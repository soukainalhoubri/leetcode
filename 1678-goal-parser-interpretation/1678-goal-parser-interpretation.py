class Solution:
    def interpret(self, command: str) -> str:
        answer=""
        n=len(command)
        for i in range(n):
            if command[i]=="(":
                if command[i+1]==")":
                    answer+="o"
                else:
                    answer+="al"
            elif command[i]=="G":
                answer+="G"
            else:
                continue
        return answer