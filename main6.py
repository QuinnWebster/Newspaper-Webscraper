from cragAndCanyonArticles import get_summary as get_cragAndCanyon_summaries
from rockyMountainOutlookArticles import get_summary as rockyMountainOutlook_summaries

def main():
    # print("Top News Summaries from the Crag and Canyon:")
    summaries_1 = get_cragAndCanyon_summaries()

    print(summaries_1)
 
    

    print("\nTop News Summaries from the Rocky Mountain Outlook:")
    summaries_2 = rockyMountainOutlook_summaries()

    print(summaries_2)
  

if __name__ == "__main__":
    main()
