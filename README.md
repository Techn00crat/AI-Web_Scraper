# AI Web Scraper

## Overview
The AI Web Scraper is a Streamlit-based application that extracts and parses data from websites using AI models. It allows users to enter a URL, scrape its content, and refine the extracted information using a description prompt. The parsed results can be downloaded in JSON or CSV format.

## Features
- **Web Scraping**: Extracts content from a given website URL.
- **AI-Powered Parsing**: Uses an AI model to process and structure the extracted content.
- **User Feedback System**: Allows users to refine extraction by providing descriptions.
- **Download Options**: Users can download results in JSON or CSV formats.

## Technologies Used
- **Python**
- **Streamlit** (for UI)
- **BeautifulSoup** (for web scraping)
- **Ollama AI Model** (for parsing extracted content)
- **Pandas** (for data processing)
- **JSON & CSV Handling** (for file generation)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Techn00crat/ai-web-scraper.git
   cd ai-web-scraper
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run main.py
   ```

## Usage
1. Enter a website URL in the text input field.
2. Click on **Scrape Site** to extract the webpage content.
3. Provide a description of what you want to extract.
4. Click **Parse Content** to get structured results.
5. Provide feedback on the results.
6. If satisfied, choose the file format (JSON/CSV) and download the extracted data.

## File Structure
```
├── scrape.py       # Contains functions for web scraping
├── parse.py        # AI model integration for parsing
├── main.py         # Streamlit application logic
├── requirements.txt # Dependencies
├── README.md       # Project documentation
```

## Future Enhancements
- Add support for more AI models.
- Improve UI/UX.
- Implement support for multiple website scraping in one session.

## License
This project is licensed under the MIT License.

## Contributing
Feel free to contribute by creating pull requests or reporting issues!

## Contact
For any queries, reach out to **om.official.17.08@example.com**.

