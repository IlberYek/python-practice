# Vowel Cleaner

while True:
    prompt = input("Type the sentence you want to clean:").strip().lower() # We convert every character to lowercase to avoid errors 
    vowels = "aeıiouöüéèêâàû"
    result = ""

    for char in prompt:
        if char not in vowels:
            result += char # We add those cleaned characters to our 'piggy bank'
    print("Cleaned sentence:", result)

