import discord
import openai
import os



intents = discord.Intents.all()
openai.api_key = os.getenv("KEY")

class Chatbot(discord.Client):
    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        input_content = message.content

        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [{"role": "user", "content": input_content}]
        )
        assistant_response = response["choices"][0]['message']["content"]
        await message.channel.send(assistant_response)
    
bot = Chatbot(intents=intents)
bot.run(os.getenv("TOKEN"))