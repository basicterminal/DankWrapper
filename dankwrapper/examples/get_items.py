import discum
import dankwrapper

client = dankwrapper(
         token = ""
)

@DankWrapper.Client.gateway.command()
def on_message(resp):
    if resp.event.message:
       if resp.parsed.auto()['author']['id'] == "REPLACE WITH DANK MEMER ID":
          if client.isShop(resp.parsed.auto()['embeds'][0]['title']):
             amount = client.get_item_amount(resp.parsed.auto()['embeds'][0]['title'])
             item   = client.get_item_name(resp.parsed.auto()['embeds'][0]['title'])
            
             print(item, amount)
          else:
             pass
            
DankWrapper.Client.gateway.run()
        
