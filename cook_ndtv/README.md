## Significance of files and folders:
### cook_ndtv
Cotains the complete code used for scraping.

### recipe_op.json
The final json output. A total of 3890 recipes.
Format : A sample entry:
```
[
  {
    "category": "breads-recipes",
    "cook_time": "25 Minutes",
    "name": "Sheer Korma",
    "tags": [
      "Dates",
      "Eid",
      "Gourmet",
      "Indian Dessert",
      "Keys Hotel",
      "Restaurant Recipes"
    ],
    "ingredients": [
      "2.5 cups full fat milk",
      "1\/4 cup fine vermicilli",
      "1\/4 cup sugar",
      "1 Tbsp butter",
      "1 Tbsp rose water",
      "A small pinch cardamom powder",
      "Nuts & Dry Fruits:",
      "2 Tbsp dates - finely chopped",
      "2 Tbsp raisins",
      "1\/3 cup cashews, almonds, pistachios, charoli nuts - chopped finely",
      ""
    ],
    "image_urls": [
      "http:\/\/www.ndtv.com\/cooks\/images\/sheer.330.jpg"
    ],
    "prep_time": null,
    "images": [
      {
        "url": "http:\/\/www.ndtv.com\/cooks\/images\/sheer.330.jpg",
        "path": "full\/e41078d236460fc990fa993c9b763b0a9616b7ae.jpg",
        "checksum": "5d77f08bb4215745b2f7c4ee1ffff7ee"
      }
    ],
    "method": [
      "Boil milk in a pan until it shrinks to almost half in volume.",
      "Meanwhile you can chop the dry fruits and nuts.",
      "Soak dates in warm milk and set aside.",
      "Heat butter in a pan and add the nuts and raisins fry till slightly browned and is crispy. Set aside.",
      "In the same pan add vermicelli and roast till golden brown.",
      "Then add half of milk and let the vermicelli get cooked.",
      "Once the vermicelli turns soft add sugar, cardamom powder, give a quick stir.",
      "Add remaining milk and let it boil in low flame.",
      "Once it is thick add the roasted nuts, dates, rose water give a stir and cook for 2mins then switch off.",
      "The Kheer thickens with time so switch off accordingly.",
      ""
    ],
    "description": "This creamy dessert is ideal for every festive occasion.The crunch of roasted nuts and raisins in each bite and cardamom-infused milk base can be achieved in a short 5-step recipe."
  }
]
```
### output
Contains a folder 'full' which contains images for all the recipes. The recipe is linked to the image (path) via the json field in the recipe entry, 'images' which contains its path, url and checksum.
