import io
import sys
import traceback
from pyrogram import Client, filters
sudo = [356520246]
@Client.on_message(filters.command("exec",["/",".","*"]) & filters.user(sudo))
async def eval(c, m):
    cmd = m.text.split(" ", maxsplit=1)[1]
    
    reply_to_ = m
    if m.reply_to_message:
        reply_to_ = m.reply_to_message

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, c, m)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = "<b>OUTPUT</b>:\n"
    final_output += f"<code>{evaluation.strip()}</code> \n"

    if len(final_output) > 4096:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "out.text"
            await reply_to_.reply_document(
                document=out_file,
                disable_notification=True
            )
    else:
        await reply_to_.reply_text(final_output)


async def aexec(code, c, m):
    
    exec(
        'async def __aexec(c, m): ' +
        ''.join(f'\n {l_}' for l_ in code.split('\n'))
    )
    return await locals()['__aexec'](c, m)
