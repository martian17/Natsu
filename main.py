def check(m):
    return m.author.id == member.id and m.guild == None

try:
    msg = await self.bot.wait_for(event='message', check=check, timeout=86400)
    flag = True
    while True:
        if msg.content in yes:
            information.update_one({"owner": ctx.author.id}, {"$push": {"members": member.id}})
            
            embed3=discord.Embed(
                description=f"You have successfully joined the clan: {data['name']}.",
                color=0x8AFF62
            )

            await member.send(embed=embed3)
            embed3.description = f"{member.mention} has accepted your invitation to join the clan: {data['name']}."
            await ctx.author.send(embed=embed3, mention_author=False)
            flag = True
            break

        elif msg.content in no:
            embed3=discord.Embed(
                description=f"You have declined the invitation.",
                color=0xFF6262
            )
            
            await member.send(embed=embed3)
            embed3.description = f"{member.mention} has declined your invitation to join the clan: {data['name']}"
            await ctx.reply(embed=embed3, mention_author=False)
            flag = True
            break

        elif flag == True:
            await member.send("That is not a valid response. Please send either `accept` or `decline`.")
            flag = False
        else:
            continue

except asyncio.TimeoutError:
    await member.send("You did not answer in time.")
    await ctx.author.send(f"You invited {member.mention} to your clan but they did not answer in time.")