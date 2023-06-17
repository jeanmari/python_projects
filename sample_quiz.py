#!/bin/python

import sys
import requests

api_url = "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple"

def main():
    #get name
    name = input("What's you name?: ")
    print(f"Hi {name}! Let's have a quiz. \n")
    score = 0
    passing_percentage = .8
    passing_score = 0
    num_of_questions = 0
    
    response = requests.get(api_url)

    if response.status_code == 200:
        questions = response.json()
        questions = questions["results"]
        num_of_questions = len(questions)
        for item in questions:
            print(item["question"]+"\n")
            item["incorrect_answers"].append(item["correct_answer"])
            #created variable for a better name
            options = item["incorrect_answers"]
            #print options for questions
            for option in options:
                print(option)
            
            answer = input("\nAnswer? ")

            #converted to lower case
            if answer.lower() == item["correct_answer"].lower():
                print("correct!!\n")
                score+=1
                continue
            else:
                print("incorrect :(")
            
            print("\n")
        
        passing_score = num_of_questions * passing_percentage

        if score >= passing_score:
            print(f"Hey {name}, you passed!! Congratulations with score of {score}/{passing_score}")
        else:
            print(f"Sorry, you failed with the score of {score}/{passing_score}")    
            



if __name__ == '__main__':
    main()