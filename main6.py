from cragAndCanyonArticles import get_summary as get_summaries_1
from rockyMountainOutlookArticles import get_summary as get_summaries_2

def main():
    # Call the main function from main2.py
    print("Top News Summaries from Source 1:")
    summaries_1 = get_summaries_1()

    print(summaries_1)
 
    

    # Call the main function from main3.py
    #print("\nTop News Summaries from Source 2:")
    #summaries_2 = get_summaries_2()
  

if __name__ == "__main__":
    main()
