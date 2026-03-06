from llm import generate_title_and_description

article = "Apple just released its new iPhone 15, featuring improved cameras and longer battery life."
print("Generating...")
result = generate_title_and_description(article)
print(result)