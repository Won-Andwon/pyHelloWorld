import fileinput, re
pat = re.compile('From: (.*) <.*?>$')
for line in fileinput.input():
    m = pat.match(line)
    if m:
        print(m.group(1))

pat = re.compile(r'[a-z\-\.]+@[a-z\-\.]+]', re.IGNORECASE)
addresses = set()
for line in fileinput.input():
    for address in pat.findall(line):
        addresses.add(address)
for address in sorted(addresses):
    print(address)

# 10-11 模板示例
import fileinput, re
field_pat = re.compile(r'\[(.+?)\]')
scope = {}


def replacement(match):
    code = match.group(1)
    try:
        return str(eval(code, scope))
    except SyntaxError:
        exec(code in scope)
        return ''

lines = []
for line in fileinput.input():
    lines.append(line)
text = ''.join(lines)

print(field_pat.sub(replacement, text))
