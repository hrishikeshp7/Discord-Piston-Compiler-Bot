mport discord
from discord.ext import commands


from pistonapi import PistonAPI


token = "token lalalalala"

bot = commands.Bot(command_prefix=".", status=discord.Status.idle)

piston = PistonAPI()



@bot.event
async def on_ready():
  print(f"{bot.user} is Online.")



@bot.command()
async def run(ctx,n,*,code):
  nm = n.lower()
  a = code.replace("```","")

  if nm=="py":
      b = (piston.execute(language="py", version="3.9", code=a))
      c = str(b)
      em = discord.Embed(title="Python Code Output!", 
        description=f'```py\nOutput:\n{c}```',
        color=discord.Color.red())
      
  elif nm=="java":
      b = (piston.execute(language="java", version="15.0.2", code=a))
      c = str(b)
      em = discord.Embed(title="Java Code Output!",
       description=f'```py\nOutput:\n{c}```',
       color=discord.Color.red())
      
  elif nm=="js":
      b = (piston.execute(language="js", version="15.10.0", code=a))
      c = str(b)
      em = discord.Embed(title="JavaScript Code Output!",
       description=f'```py\nOutput:\n{c}```',
       color=discord.Color.red())
      
  elif nm=="go":
      b = (piston.execute(language="go", version="1.16.2", code=a))
      c = str(b)
      em = discord.Embed(title="Go Code Output!",
       description=f'```py\nOutput:\n{c}```',
       color=discord.Color.red())
 
  elif nm=="ts":
      b = (piston.execute(language="typescript", version="4.2.3", code=a))
      c = str(b)
      em = discord.Embed(title="TypeScript Code Output!", 
        description=f'```py\nOutput:\n{c}```',
        color=discord.Color.red())
     
  elif nm=="bf":
      b = (piston.execute(language="brainfuck", version="2.7.3", code=a))
      c = str(b)
      em = discord.Embed(title="BrainFuck Code Output!",
       description=f'```py\nOutput:\n{c}```',
       color=discord.Color.red())
      
  else:
      em = discord.Embed(title="**Not a supported language!!**")

  await ctx.send(embed=em)




bot.run(token)
   
