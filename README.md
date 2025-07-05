# LLM_extractor
# 🚀 AI-Powered Reinsurance Document Processor

## Project Overview

An intelligent document processing system that leverages **deepseeks's deepseek/deepseek-r1-0528:free model** to automatically extract structured data from reinsurance documents. The application combines modern web technologies with advanced AI to transform unstructured DOCX files into organized, queryable data formats.

## ✨ Key Features

### 🎯 **Intelligent Data Extraction**
- **AI-Powered Processing**: Uses deepseeks's "deepseek/deepseek-r1-0528:free" model models via OpenRouter API for sophisticated document understanding
- **Smart Field Recognition**: Automatically identifies and extracts 20+ specific insurance fields including policy details, coverage types, and financial information
- **Multi-Language Support**: Preserves original language and formatting from documents
- **Structured Output**: Returns clean JSON with proper data types and formatting

### 🎨 **Modern Web Interface**
- **Responsive Design**: Beautiful, mobile-friendly interface with glassmorphism effects
- **Drag & Drop Upload**: Intuitive file handling with visual feedback
- **Real-time Processing**: Live status updates during document analysis
- **Interactive Results**: Organized data display with expandable sections and statistics

### 🔧 **Technical Architecture**
- **Backend**: Flask-based REST API with robust error handling
- **Frontend**: Pure HTML/CSS/JavaScript with modern UI patterns
- **Document Processing**: Python-docx for DOCX file parsing
- **AI Integration**: OpenRouter API for GPT model access
- **Data Flow**: Secure temporary file handling with automatic cleanup

## 🛠 Technical Stack

### Backend Technologies
- **Flask** - Lightweight web framework
- **Python-docx** - DOCX document parsing
- **OpenAI SDK** - AI model integration
- **Tempfile** - Secure file handling

### Frontend Technologies
- **HTML5** - Modern semantic markup
- **CSS3** - Advanced styling with gradients, animations, and responsive design
- **Vanilla JavaScript** - Clean, dependency-free interactions
- **Drag & Drop API** - Native file handling

### AI & Data Processing
- **OpenRouter API** - Access to multiple AI models
- **DeepSeek R1** - Primary model for document analysis
- **JSON Schema Validation** - Structured data output
- **Intelligent Prompting** - Context-aware field extraction

## 🏗 System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Browser   │───▶│   Flask API     │───▶│   AI Service    │
│   (Frontend)    │    │   (Backend)     │    │  (OpenRouter)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                        │                        │
         │                        ▼                        │
         │              ┌─────────────────┐               │
         │              │ Document Parser │               │
         │              │  (python-docx)  │               │
         │              └─────────────────┘               │
         │                        │                        │
         └────────────────────────┼────────────────────────┘
                                  ▼
                        ┌─────────────────┐
                        │ Structured Data │
                        │    (JSON)       │
                        └─────────────────┘
```

## 📊 Data Processing Pipeline

1. **Document Upload**: Secure file handling with validation
2. **Text Extraction**: Parse DOCX structure including tables and paragraphs
3. **AI Analysis**: Intelligent field identification using context-aware prompts
4. **Data Structuring**: Convert unstructured text to structured JSON
5. **Results Display**: Interactive visualization with statistics and formatting

## 🎯 Extracted Fields

The system intelligently extracts 20+ specific insurance fields:

### Business Information
- Business Source, Original Insured Name, Broker Name, Reinsured Name
- Insured Address, Type of Contract

### Policy Details
- Policy Duration, Validity Dates, Currency, Exchange Rate
- Territorial Limits, Reinsurance Scheme

### Financial Information
- Maximum Contract Limit, Total Sum Insured, Number of Insured
- Reinsurance Commission, Premium Payment Frequency

### Coverage Details
- Coverage Types (as arrays), Special Clauses

## 🔥 Advanced Features

### Smart UI Components
- **Visual Statistics Dashboard**: Real-time completion metrics
- **Collapsible Raw Data View**: Toggle between formatted and JSON views
- **Responsive Grid Layout**: Adaptive design for all screen sizes
- **Loading States**: Smooth transitions and progress indicators

### Robust Error Handling
- **File Type Validation**: Accepts only DOCX files
- **API Error Management**: Graceful handling of AI service failures
- **Temporary File Cleanup**: Automatic resource management
- **User-Friendly Messages**: Clear error communication

### Performance Optimizations
- **Efficient File Processing**: Minimal memory footprint
- **Async Operations**: Non-blocking UI during processing
- **Smart Caching**: Optimized API calls with proper parameters

## 🌟 Technical Highlights

### Modern Development Practices
- **Clean Architecture**: Separation of concerns between frontend and backend
- **RESTful API Design**: Standard HTTP methods and status codes
- **Secure File Handling**: Temporary file management with automatic cleanup
- **Error Boundary Implementation**: Comprehensive error handling at all levels

### AI Integration Excellence
- **Intelligent Prompting**: Context-aware field extraction with examples
- **Model Flexibility**: Easy switching between different AI models
- **Structured Output**: JSON schema validation for consistent results
- **Temperature Control**: Optimized for accuracy vs creativity balance

### User Experience Focus
- **Progressive Enhancement**: Works without JavaScript for basic functionality
- **Accessibility**: Proper ARIA labels and semantic HTML
- **Mobile-First Design**: Responsive layout for all devices
- **Visual Feedback**: Clear indicators for all user actions

## 🚀 Performance Metrics

- **Processing Speed**: ~10-30 seconds per document (depending on complexity)
- **Accuracy Rate**: High precision field extraction using AI models
- **File Size Support**: Handles standard business document sizes efficiently
- **Browser Compatibility**: Works across modern browsers with fallbacks

## 💡 Innovation Points

1. **AI-First Approach**: Leverages cutting-edge language models for document understanding
2. **No-Code Field Addition**: Easy to extend with new fields through prompt engineering
3. **Visual Data Presentation**: Transforms raw data into business-ready insights
4. **Scalable Architecture**: Built for enterprise-level document processing needs

This project demonstrates expertise in **full-stack development**, **AI integration**, **modern web technologies**, and **user experience design**, making it an excellent showcase of contemporary software engineering practices.
