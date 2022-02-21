import discum
import time, os, random, colorama, requests

class DankBase:
      API = "https://discordapp.com/api/v9"  
    
class DankWrapper:
      Client  = ""
      Session = {
              "Token" : "",
              "Author": {}
      }
    
      def __init__(self, 
                   Token = "") -> str: ## Login ##
          DankWrapper.Client = discum.Client(
                               log   = False,
                               token = Token
          )
          
          if requests.get("%s/users/@me" % (DankBase.API), headers = {"Authorization": token}).status_code in [200, 201, 203, 204]:
             DankWrapper.Session["Token"]  = Token
             DankWrapper.Session["Author"] = "Error"
             
          else:
             exit(print(
                  "[!] %sImproper Token Passed%s" % (colorama.Fore.RED, colorama.Fore.RESET)
                  ))
      
      def get_items_from_inventory(
          self,
          unparsed_items = "") -> list: ## This has not been tested, may not work ##
                                  if DankWrapper.Session["Token"] != "":
                                     items   = []
                                     content = []
                                     
                                     for item in unparsed_items.split("─"):
                                         item_name     = item[0].split(">")[1].replace(" ", "")
                                         item_quantity = item[1]
                                         
                                         items   += ["%s, %s" % (item_name, item_quantity)]
                                         content += ["%s:%s" % (item_name, item_quantity)]
                                
                                     return items
                  
      def get_item_count(
          self,
          unparsed_title = "") -> str: ## Most likely works after no tests ##
                                  if DankWrapper.Session["Token"] != "":
                                     try:
                                        return unparsed_title.split("(")[0].replace("owned)", "")
                                     except:
                                        return "Not Detectable"
                                  else:
                                     exit(print(
                                          "[!] %sPlease Log-In%s" % (colorama.Fore.RED, colorama.Fore.RESET)
                                          ))
      def start_discum_client():
          DankWrapper.Client.gateway.run()
                                     
                  
          
