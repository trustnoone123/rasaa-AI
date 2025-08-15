def save_pdf_as_product(pdf_data: dict):
    """
    Store a PDF file as a Product node in Neo4j using the provided query and params structure.
    Expects pdf_data to have keys: 'Product Name', 'Brand', 'Price', 'Discount', 'Availability',
    'Rating', 'Review Count', 'Product URL', 'Category'.
    """
    query = """
    MERGE (p:Product {name: $name})
    SET p += {
        brand: $brand,
        price: $price,
        discount: $discount,
        availability: $availability,
        rating: $rating,
        review_count: $review_count,
        url: $url,
        category: $category
    }
    """
    params = {
        "name": pdf_data.get("Product Name", ""),
        "brand": pdf_data.get("Brand", ""),
        "price": pdf_data.get("Price", ""),
        "discount": pdf_data.get("Discount", ""),
        "availability": pdf_data.get("Availability", ""),
        "rating": pdf_data.get("Rating", ""),
        "review_count": pdf_data.get("Review Count", ""),
        "url": pdf_data.get("Product URL", ""),
        "category": pdf_data.get("Category", "")
    }
    with driver.session(database=NEO4J_DATABASE) as session:
        session.run(query, params)
from neo4j import GraphDatabase, Driver
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()  # Load credentials from .env

NEO4J_URI="neo4j+ssc://99ac5f56.databases.neo4j.io"
NEO4J_USER="neo4j"
NEO4J_PASSWORD="2OOPeeZBMU_ZcaJSB7iyRSvcvuRo1rENZG1mZLtxgxY"
NEO4J_DATABASE="neo4j"

driver: Driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))


def save_product_to_neo4j(product: dict):
    """Insert or update a product node in the Neo4j graph."""
    query = """
    MERGE (p:Product {name: $name})
    SET p += {
        brand: $brand,
        price: $price,
        discount: $discount,
        availability: $availability,
        rating: $rating,
        review_count: $review_count,
        url: $url,
        category: $category
    }
    """
    params = {
        "name": product["Product Name"],
        "brand": product.get("Brand", ""),
        "price": product.get("Price", ""),
        "discount": product.get("Discount", ""),
        "availability": product.get("Availability", ""),
        "rating": product.get("Rating", ""),
        "review_count": product.get("Review Count", ""),
        "url": product.get("Product URL", ""),
        "category": product.get("Category", "")
    }

    with driver.session(database=NEO4J_DATABASE) as session:
        session.run(query, params)


def save_pdf_document_to_neo4j(pdf_data: dict):
    """
    Save PDF document and its extracted content to Neo4j database.
    
    Args:
        pdf_data: Dictionary containing PDF metadata and extracted content
    """
    # Create PDF Document node
    doc_query = """
    MERGE (d:Document {filename: $filename})
    SET d += {
        title: $title,
        author: $author,
        subject: $subject,
        creator: $creator,
        producer: $producer,
        creation_date: $creation_date,
        modification_date: $modification_date,
        page_count: $page_count,
        file_size: $file_size,
        upload_timestamp: $upload_timestamp,
        document_type: $document_type,
        estimated_word_count: $estimated_word_count,
        has_tables: $has_tables,
        has_numbers: $has_numbers,
        language: $language
    }
    """
    
    doc_params = {
        "filename": pdf_data['filename'],
        "title": pdf_data['metadata']['title'],
        "author": pdf_data['metadata']['author'],
        "subject": pdf_data['metadata']['subject'],
        "creator": pdf_data['metadata']['creator'],
        "producer": pdf_data['metadata']['producer'],
        "creation_date": pdf_data['metadata']['creation_date'],
        "modification_date": pdf_data['metadata']['modification_date'],
        "page_count": pdf_data['metadata']['page_count'],
        "file_size": pdf_data['file_size'],
        "upload_timestamp": datetime.now().isoformat(),
        "document_type": pdf_data.get('key_info', {}).get('document_type', 'PDF'),
        "estimated_word_count": pdf_data.get('key_info', {}).get('estimated_word_count', 0),
        "has_tables": pdf_data.get('key_info', {}).get('has_tables', False),
        "has_numbers": pdf_data.get('key_info', {}).get('has_numbers', False),
        "language": pdf_data.get('key_info', {}).get('language', 'English')
    }
    
    with driver.session(database=NEO4J_DATABASE) as session:
        # Create document node
        session.run(doc_query, doc_params)
        
        # Create content nodes for each page
        for page_data in pdf_data['text_content']:
            content_query = """
            MATCH (d:Document {filename: $filename})
            MERGE (c:Content {page_number: $page_number, document_filename: $filename})
            SET c.text = $text
            MERGE (d)-[:HAS_CONTENT]->(c)
            """
            
            content_params = {
                "filename": pdf_data['filename'],
                "page_number": page_data['page'],
                "text": page_data['text']
            }
            
            session.run(content_query, content_params)
        
        # Create topic nodes and relationships
        if 'key_info' in pdf_data and 'main_topics' in pdf_data['key_info']:
            for topic in pdf_data['key_info']['main_topics']:
                topic_query = """
                MATCH (d:Document {filename: $filename})
                MERGE (t:Topic {name: $topic_name})
                MERGE (d)-[:HAS_TOPIC]->(t)
                """
                
                topic_params = {
                    "filename": pdf_data['filename'],
                    "topic_name": topic
                }
                
                session.run(topic_query, topic_params)
        
        # Create key phrase nodes and relationships
        if 'key_info' in pdf_data and 'key_phrases' in pdf_data['key_info']:
            for phrase in pdf_data['key_info']['key_phrases']:
                phrase_query = """
                MATCH (d:Document {filename: $filename})
                MERGE (p:KeyPhrase {phrase: $phrase_text})
                MERGE (d)-[:HAS_KEY_PHRASE]->(p)
                """
                
                phrase_params = {
                    "filename": pdf_data['filename'],
                    "phrase_text": phrase
                }
                
                session.run(phrase_query, phrase_params)


def get_pdf_documents():
    """Retrieve all PDF documents from the database."""
    query = """
    MATCH (d:Document)
    OPTIONAL MATCH (d)-[:HAS_TOPIC]->(t:Topic)
    OPTIONAL MATCH (d)-[:HAS_KEY_PHRASE]->(kp:KeyPhrase)
    RETURN d, 
           collect(DISTINCT t.name) as topics,
           collect(DISTINCT kp.phrase) as key_phrases
    ORDER BY d.upload_timestamp DESC
    """
    
    with driver.session(database=NEO4J_DATABASE) as session:
        result = session.run(query)
        return [record.data() for record in result]


def search_pdf_content(search_term: str):
    """Search for PDF content containing specific terms."""
    query = """
    MATCH (c:Content)
    WHERE c.text CONTAINS $search_term
    MATCH (d:Document)-[:HAS_CONTENT]->(c)
    RETURN d.filename as filename, 
           c.page_number as page,
           c.text as content,
           d.title as title
    ORDER BY d.upload_timestamp DESC
    """
    
    with driver.session(database=NEO4J_DATABASE) as session:
        result = session.run(query, {"search_term": search_term})
        return [record.data() for record in result]


def run_query(cypher_query: str, parameters: dict = None):
    """Run a Cypher query and return the results as a list of dictionaries."""
    with driver.session(database=NEO4J_DATABASE) as session:
        result = session.run(cypher_query, parameters or {})
        return [record.data() for record in result]


# Optional: for testing
if __name__ == "__main__":
    product = {
        "Product Name": "Example Product",
        "Brand": "BrandX",
        "Price": "100",
        "Discount": "10%",
        "Availability": "In Stock",
        "Rating": "4.5",
        "Review Count": "100",
        "Product URL": "http://example.com",
        "Category": "CategoryX"
    }
    save_product_to_neo4j(product)
    print("✅ Product saved.")
