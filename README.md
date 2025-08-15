# PDF to DB Converter with Conversational Agent

A streamlined application that combines PDF document processing with an intelligent conversational agent. Upload PDFs to Neo4j database and interact with your documents through natural conversation.

## 🚀 Features

### 1. PDF to Database Converter
- **PDF Upload & Processing**: Upload PDF files through an intuitive interface
- **Text Extraction**: Extract text content and metadata from PDFs using PyPDF2 and pdfplumber
- **Neo4j Storage**: Store PDF documents, content, and extracted information in Neo4j graph database
- **Smart Analysis**: Automatically extract key information, topics, and phrases from documents

### 2. Conversational Agent
- **Natural Language Interface**: Ask questions about your documents in plain English
- **Context Awareness**: The agent understands your uploaded PDFs and database structure
- **Suggested Actions**: Get intelligent suggestions for next steps and queries
- **Conversation History**: Maintain context across your entire conversation session

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Streamlit     │    │  Conversational  │    │     Neo4j       │
│   Frontend      │◄──►│      Agent       │◄──►│   Database      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         │              ┌──────────────────┐            │
         └─────────────►│   PDF Processor  │            │
                        └──────────────────┘            │
                                 │                      │
                                 └──────────────────────┘
```

## 📋 Prerequisites

- Python 3.8+
- Neo4j Database (local or cloud)
- OpenAI API Key

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Conversational-Agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp env.example .env
   ```
   
   Edit `.env` with your credentials:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   NEO4J_URI=bolt://localhost:7687
   NEO4J_USER=neo4j
   NEO4J_PASSWORD=your_password
   ```

4. **Start Neo4j database**
   - Local: Start Neo4j Desktop or Docker container
   - Cloud: Use Neo4j AuraDB or other cloud service

## 🚀 Usage

### Starting the Application
```bash
streamlit run app.py
```

### Basic Workflow
1. **Upload PDF**: Use the PDF upload section to add documents
2. **Process & Store**: Click "Process & Store PDF" to extract content and save to Neo4j
3. **Chat**: Ask questions about your documents using the conversational interface
4. **Explore**: View uploaded documents and their extracted information

### Example Conversations
- "What documents do I have?"
- "Analyze the uploaded PDF"
- "What are the main topics in my documents?"
- "Help me understand the content structure"

## 🗄️ Database Schema

The application creates the following Neo4j nodes and relationships:

```
(Document)-[:HAS_CONTENT]->(Content)
(Document)-[:HAS_TOPIC]->(Topic)
(Document)-[:HAS_KEY_PHRASE]->(KeyPhrase)
```

**Document Node Properties:**
- filename, title, author, page_count, file_size, upload_timestamp, key_info

**Content Node Properties:**
- page_number, text_content

**Topic Node Properties:**
- topic_name

**KeyPhrase Node Properties:**
- phrase_text

## ⚙️ Configuration

### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key for GPT-4 access
- `NEO4J_URI`: Neo4j database connection URI
- `NEO4J_USER`: Neo4j username
- `NEO4J_PASSWORD`: Neo4j password

### Customization
- Modify `utils/pdf_processor.py` to enhance PDF text extraction
- Update `llm/conversational_agent.py` to customize the AI agent's behavior
- Adjust Neo4j schema in `db/neo4j_client.py` for different data structures

## 🔧 Troubleshooting

### Common Issues
1. **Neo4j Connection Error**
   - Verify database is running
   - Check connection credentials in `.env`
   - Ensure firewall allows connection

2. **PDF Processing Errors**
   - Verify PDF file is not corrupted
   - Check if PDF is password-protected
   - Ensure sufficient memory for large files

3. **OpenAI API Errors**
   - Verify API key is valid
   - Check API quota and billing
   - Ensure internet connectivity

### Debug Mode
Enable debug logging by setting environment variable:
```bash
export STREAMLIT_LOG_LEVEL=debug
```

## 🚀 Future Enhancements

- **Advanced NLP**: Integrate spaCy or NLTK for better text analysis
- **Document Search**: Full-text search across all uploaded documents
- **Batch Processing**: Upload and process multiple PDFs simultaneously
- **Export Features**: Export processed data to various formats
- **User Management**: Multi-user support with document sharing

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For support and questions, please open an issue in the repository. 