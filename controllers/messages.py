from agent.__init__ import agent, ctx

async def new_msg(msg):
    response = await agent.run(msg.msg, ctx=ctx)
    response = str(response)
    return {"text": response}