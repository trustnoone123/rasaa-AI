# 🤖 AI-Powered Document & Graph Assistant

An enhanced conversational AI assistant that combines PDF document processing, Neo4j graph database integration, and intelligent conversation capabilities.

## ✨ New Features Added

### 📄 PDF Document Management
- **PDF Upload & Processing**: Upload PDF files through an intuitive interface
- **Text Extraction**: Extract text content and metadata from PDF documents
- **Content Analysis**: Automatically identify key topics, phrases, and document characteristics
- **Neo4j Storage**: Store PDF content, metadata, and extracted information in Neo4j graph database
- **Content Search**: Search through uploaded PDF content using natural language queries

### 💬 Enhanced Conversational Agent
- **Two-Way Communication**: Maintains conversation context and provides intelligent responses
- **Context Awareness**: Remembers previous conversations and uses them for better responses
- **Smart Suggestions**: Provides relevant action suggestions based on conversation context
- **Multi-Modal Support**: Handles questions about PDFs, database queries, and general assistance
- **Conversation History**: View and manage conversation history with summary capabilities

### 🔍 Advanced Query Capabilities
- **Cypher Query Generation**: Convert natural language to Neo4j Cypher queries
- **Content Search**: Search PDF documents for specific terms or phrases
- **Database Statistics**: Get real-time statistics about your data
- **Quick Actions**: Streamlined interface for common operations

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Neo4j database (local or cloud)
- OpenAI API key

### Installation

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
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   NEO4J_URI=your_neo4j_connection_string
   NEO4J_USER=your_neo4j_username
   NEO4J_PASSWORD=your_neo4j_password
   NEO4J_DATABASE=neo4j
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📖 Usage Guide

### PDF Document Management

#### Uploading a PDF
1. Use the sidebar to upload a PDF file
2. Click "Process & Store PDF" to extract content and store in Neo4j
3. View processing results and extracted information

#### Viewing Uploaded Documents
- All uploaded PDFs are displayed in the sidebar
- Click on any document to view its metadata and extracted content
- See page count, word count, and identified topics

#### Searching PDF Content
- Use the "Search PDF Content" section in the right column
- Enter search terms to find specific content across all documents
- Results show filename, page number, and matching content

### Conversational Assistant

#### Starting a Conversation
- Type your questions in the main chat interface
- Ask about uploaded documents, database queries, or general assistance
- The agent maintains context throughout the conversation

#### Suggested Actions
- The agent provides relevant action suggestions
- Click on suggestions to automatically execute them
- Suggestions are context-aware and change based on conversation

#### Managing Conversations
- Clear chat history using the sidebar button
- View conversation summary for insights
- All conversations are maintained in session state

### Database Operations

#### Cypher Query Generation
- Describe what you want to query in natural language
- The system generates appropriate Cypher queries
- Execute queries directly from the interface
- View results in JSON format

#### Database Statistics
- Get real-time counts of documents, products, and parts
- Monitor database health and content
- Track uploaded document metrics

## 🏗️ Architecture

### Core Components

```
Conversational-Agent/
├── app.py                          # Main Streamlit application
├── llm/
│   ├── conversational_agent.py    # Enhanced conversational AI
│   └── query.py                   # Cypher query generation
├── db/
│   └── neo4j_client.py           # Database operations
├── utils/
│   ├── pdf_processor.py          # PDF processing utilities
│   └── tts.py                    # Text-to-speech functionality
└── requirements.txt               # Python dependencies
```

### Data Flow

1. **PDF Upload** → PDF Processor → Content Extraction → Neo4j Storage
2. **User Query** → Conversational Agent → Context Analysis → Response Generation
3. **Database Query** → Cypher Generation → Neo4j Execution → Result Display

### Neo4j Schema

The system creates the following graph structure:

```
(:Document)-[:HAS_CONTENT]->(:Content)
(:Document)-[:HAS_TOPIC]->(:Topic)
(:Document)-[:HAS_KEY_PHRASE]->(:KeyPhrase)
(:Product)-[:USED_IN]->(:BikeModel)
(:Part)-[:USED_IN]->(:BikeModel)
(:BikeModel)-[:IS_A]->(:BikeType)
```

## 🔧 Configuration

### OpenAI Settings
- Model: GPT-4 (configurable in `conversational_agent.py`)
- Temperature: 0.7 (balanced creativity and accuracy)
- Max tokens: 500 (response length limit)

### PDF Processing
- Supports both PyPDF2 and pdfplumber for text extraction
- Automatic fallback if primary extraction method fails
- Configurable text analysis parameters

### Neo4j Connection
- Connection pooling for better performance
- Automatic session management
- Error handling and retry logic

## 🧪 Testing

Run the test suite to verify all features:

```bash
python test_features.py
```

This will test:
- Module imports
- PDF processing functionality
- Conversational agent capabilities
- Neo4j client functions

## 🚨 Troubleshooting

### Common Issues

1. **PDF Processing Errors**
   - Ensure PDF is not password-protected
   - Check file size limits
   - Verify PDF is not corrupted

2. **Neo4j Connection Issues**
   - Verify connection credentials
   - Check network connectivity
   - Ensure database is running

3. **OpenAI API Errors**
   - Verify API key is valid
   - Check API quota and limits
   - Ensure proper environment variable setup

### Performance Tips

- Use smaller PDFs for faster processing
- Clear conversation history periodically
- Monitor Neo4j query performance
- Use appropriate indexes for large datasets

## 🔮 Future Enhancements

- **Multi-language Support**: Process PDFs in different languages
- **Advanced NLP**: Better topic extraction and content analysis
- **Document Comparison**: Compare multiple PDFs for similarities
- **Export Functionality**: Export processed data and insights
- **API Integration**: REST API for external applications
- **Real-time Collaboration**: Multi-user document analysis

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📞 Support

For support and questions:
- Open an issue on GitHub
- Check the troubleshooting section
- Review the configuration documentation

---

**Happy Document Analysis! 🎉** 