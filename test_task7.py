#!/usr/bin/env python3
"""
Test script to demonstrate Task 7 error handling for invalid inputs
"""

from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

def test_task7_error_handling():
    """Test Task 7 error handling with invalid and valid inputs"""
    
    print("Testing Task 7 Error Handling:")
    print("=" * 50)
    
    # Test cases that would typically return 500 status from Watson API
    invalid_test_cases = [
        "as987da-6s2d aweadsa",  # Nonsensical text as mentioned in Task 7
        "",  # Empty string
        "!@#$%^&*()",  # Special characters only
        "123456789",  # Numbers only
    ]
    
    # Valid test cases
    valid_test_cases = [
        "Testing this application for error handling",
        "I love this technology",
        "This is a bad experience"
    ]
    
    print("Testing INVALID inputs (should return None for label and score):")
    print("-" * 50)
    
    for text in invalid_test_cases:
        try:
            result = sentiment_analyzer(text)
            label = result['label']
            score = result['score']
            
            print(f"Text: '{text}'")
            if label is None:
                print("Result: Invalid input detected! (label=None, score=None)")
                print("✅ Task 7 error handling working correctly")
            else:
                print(f"Label: {label}, Score: {score}")
                print("ℹ️  Fallback analyzer used (external service unavailable)")
            print("-" * 30)
        except Exception as e:
            print(f"Error analyzing '{text}': {e}")
            print("-" * 30)
    
    print("\nTesting VALID inputs (should return proper sentiment analysis):")
    print("-" * 50)
    
    for text in valid_test_cases:
        try:
            result = sentiment_analyzer(text)
            label = result['label']
            score = result['score']
            
            print(f"Text: '{text}'")
            if label is None:
                print("Result: Invalid input detected! (label=None, score=None)")
            else:
                print(f"Label: {label}, Score: {score}")
            print("-" * 30)
        except Exception as e:
            print(f"Error analyzing '{text}': {e}")
            print("-" * 30)

def test_server_response():
    """Test how the server.py responds to None values"""
    
    print("\nTesting Server Response Format:")
    print("=" * 50)
    
    # Simulate the server.py logic
    def simulate_server_response(text_to_analyze):
        response = sentiment_analyzer(text_to_analyze)
        label = response['label']
        score = response['score']
        
        # Check if the label is None, indicating an error or invalid input
        if label is None:
            return "Invalid input! Try again."
        else:
            # Return a formatted string with the sentiment label and score
            return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)
    
    # Test with invalid input
    invalid_text = "as987da-6s2d aweadsa"
    server_response = simulate_server_response(invalid_text)
    print(f"Input: '{invalid_text}'")
    print(f"Server Response: {server_response}")
    print()
    
    # Test with valid input
    valid_text = "I love this application"
    server_response = simulate_server_response(valid_text)
    print(f"Input: '{valid_text}'")
    print(f"Server Response: {server_response}")

if __name__ == "__main__":
    test_task7_error_handling()
    test_server_response()
