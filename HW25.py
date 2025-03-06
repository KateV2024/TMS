import requests


# Get postid=80

url = "https://jsonplaceholder.typicode.com/posts/80"
post_80 = requests.get(url)

if post_80.status_code == 200:
    print(post_80.json())
else:
    print(f"Error for getting postid=80: {post_80.status_code}")

#  Get comments for postId=60
url_1 = "https://jsonplaceholder.typicode.com/comments?postId=60"
comments_to_postid_60 = requests.get(url_1)

if comments_to_postid_60.status_code == 200:
    print(comments_to_postid_60.json())
else:
    print(f"Error for getting comments for postid=60: {comments_to_postid_60.status_code}")

# Create a new post
url_2 = "https://jsonplaceholder.typicode.com/posts"
new_post = requests.post(url_2)

if new_post.status_code == 201:
    print(new_post.json())
else:
    print(f"Error for creating a new post: {new_post.status_code}")

# delete postId=7
url_3 = "https://jsonplaceholder.typicode.com/posts/7"
delete_post= requests.delete(url_3)

if delete_post.status_code == 200:
    print("PostId=7 is deleted")
else:
    print(f"Error for deleting postId=7")

# Get a random cat
cat_url = "https://api.thecatapi.com/v1/images/search"
random_cat = requests.get(cat_url)

if random_cat.status_code == 200:
    data = random_cat.json()
    cat_image_url = data[0]["url"]  # Extract the image URL
    print("Random Cat Image URL:", cat_image_url, random_cat.json())
else:
    print(f"Error: {random_cat.status_code}")

# Vote for a cat

import requests

# Get a random cat
cat_url = "https://api.thecatapi.com/v1/images/search"
random_cat = requests.get(cat_url)

if random_cat.status_code == 200:
    data = random_cat.json()  # Store the JSON response
    cat_image_url = data[0]["url"]  # Extract image URL
    cat_img_id = data[0]["id"]  # Extract image ID (needed for voting)

    print("Random Cat Image URL:", cat_image_url)
else:
    print(f"❌ Error: {random_cat.status_code}")

# Vote for the cat
vote_url = "https://api.thecatapi.com/v1/votes"
api_key = "live_MlAAPB8rNxjx3XFN5rnYR8HopL3a8FVOp9ZTFMF7w19jUdJfozgpyQTz041YLyLT"

# Prepare vote data
vote_data = {
    "image_id": cat_img_id,
    "value": 10
}

headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key
}

voting_response = requests.post(vote_url, json=vote_data, headers=headers)

if voting_response.status_code == 201:
    print("✅ Successfully voted for the cat!")
    print("Response:", voting_response.json())
else:
    print(f"❌ Error: {voting_response.status_code}")
    print(voting_response.json())

# Delete a cat from favourite
url_4 = "https://api.thecatapi.com/v1/favourites"
new_data = {
    "image_id": cat_img_id
}

favourite = requests.post(url_4, json=new_data, headers=headers)
fav_id = favourite.json()["id"]
print(fav_id)

url_5 = f"https://api.thecatapi.com/v1/favourites/{fav_id}"
delete_from_vav = requests.delete(url_5, json=new_data, headers=headers)

if delete_from_vav.status_code == 200:
    print("✅ Cat is deleted from favourite!")
    print("Response:", delete_from_vav.json())
else:
    print(f"❌ Error: {delete_from_vav.status_code}")
    print(delete_from_vav.json())