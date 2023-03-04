import requests
import json
import colorama
response_api = requests.get("https://newsapi.org/v2/top-headlines/sources?apiKey=673460c6763141d785fd3c01cf233985")

print(response_api.status_code)

NewsData = response_api.text

parse_json = json.loads(NewsData)


while True:
    print("\nChoose Your Favourite Category News: \n")
    print("1: general")
    print("2: business")
    print("3: technology")
    print("4: sports")
    print("5: entertainment")
    print("6: science")
    
    cat = int(input("Enter Your Category: "))

    match cat:

        case 1: 
            c = 1
            while c <= 40:
                if(parse_json["sources"][c]["category"] == "general"):
                    print(colorama.Fore.YELLOW+"\nCategory: ",parse_json["sources"][c]["category"],"\n")
                    print(parse_json["sources"][c]["description"])
                c += 1
        case 2: 
            c = 1
            while c <= 40:
                if(parse_json["sources"][c]["category"] == "business"):
                    print(colorama.Fore.YELLOW+"\nCategory: ",parse_json["sources"][c]["category"],"\n")
                    print(parse_json["sources"][c]["description"])
                c += 1

        case 3: 
            c = 1
            while c <= 40:
                if(parse_json["sources"][c]["category"] == "technology"):
                    print(colorama.Fore.YELLOW+"\nCategory: ",parse_json["sources"][c]["category"],"\n")
                    print(parse_json["sources"][c]["description"])
                c += 1

        case 4: 
            c = 1
            while c <= 40:
                if(parse_json["sources"][c]["category"] == "sports"):
                    print(colorama.Fore.YELLOW+"\nCategory: ",parse_json["sources"][c]["category"],"\n")
                    print(parse_json["sources"][c]["description"])
                c += 1

        case 5: 
            c = 1
            while c <= 40:
                if(parse_json["sources"][c]["category"] == "entertainment"):
                    print(colorama.Fore.YELLOW+"\nCategory: ",parse_json["sources"][c]["category"],"\n")
                    print(parse_json["sources"][c]["description"])
                c += 1
        case 6: 
            c = 1
            while c <= 40:
                if(parse_json["sources"][c]["category"] == "science"):
                    print(colorama.Fore.YELLOW+"\nCategory: ",parse_json["sources"][c]["category"],"\n")
                    print(parse_json["sources"][c]["description"])
                c += 1
   



