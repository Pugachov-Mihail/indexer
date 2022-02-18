from dipdup.context import HookContext

async def on_rollback(
    ctx: HookContext,
) -> None:
    await ctx.execute_sql('on_rollback')