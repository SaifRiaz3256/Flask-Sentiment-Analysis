#!/usr/bin/env python3
"""
Simple test script to verify the fallback sentiment analyzer works
"""

from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

def test_fallback_analyzer():
    """Test the fallback sentiment analyzer with various text samples"""
    
    test_cases = [
        "I love this new technology!",
        "This is terrible and awful",
        "The weather is okay today",
        "I am so happy and excited about this amazing project!",
        "I hate this stupid and boring task",
        "Hello world"
    ]
    
    print("Testing Sentiment Analysis (with fallback):")
    print("=" * 50)
    
    for text in test_cases:
        try:
            result = sentiment_analyzer(text)
            print(f"Text: '{text}'")
            print(f"Label: {result['label']}")
            print(f"Score: {result['score']:.3f}")
            print("-" * 30)
        except Exception as e:
            print(f"Error analyzing '{text}': {e}")
            print("-" * 30)

if __name__ == "__main__":
    test_fallback_analyzer()
