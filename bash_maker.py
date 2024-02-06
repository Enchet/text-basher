inp_text = open("input.txt").read().replace("\n", "")
divided_text = inp_text.split(".")
echo_text =  []
for sentence in divided_text:
    echo_text.append("echo " + sentence)

with open('output.txt', 'w') as f:
    for line in echo_text:
        f.write(f"{line}\n")
        f.write(f"wait(1)\n")