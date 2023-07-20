class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        p_subs = ''
        for i in range(n):
            for j in range(i+1, n+1):
                # print(f"i: {i}\nj:{j}")
                temp = s[i:j]
                # print(temp)
                if temp == temp[::-1]:
                    if len(temp) > len(p_subs):
                        p_subs = temp
        print(p_subs)
        return p_subs


s = Solution()
s.longestPalindrome("vyzonecajxxdvswhftixmzgjbfoeilbnchqmdgoxfmkkkkcqguavfozmplhzgothrwpukzgkctdacbxefrzrmbgwwrrhpcvqwvgwgknyrtxxoligsqpbqoucltakbkywwssyodzydsjxeuvgiqqitkfkqnxsfflgbjvbxdrworsdkowtkgabnszgsmgytupybdclmmsmougfendwvzarfdfbixjnlxvevqfoohcgrrysofifdfulygrmkwpimduzzluojeqixdtcxhcqnfsdbunmhsglhiplgbhrqrrrprffjfradvbifxxhoqylkejyprxdtianietnjumltxywfowopghurofvwtxvaxtqnjbzwvljjwfmmlhixogwwyaoysvrpgfymyqjschhqcwvytkreirdxfapaomayebhkzxgmlthoxialmtnilfopvhhqlocytyrtpfmpgqakdbrsteurcpfvruicuxzukfpwjwgnuaaungwjwpfkuzxuciurvfpcruetsrbdkaqgpmfptrytycolqhhvpoflintmlaixohtlmgxzkhbeyamoapafxdrierktyvwcqhhcsjqymyfgprvsyoaywwgoxihlmmfwjjlvwzbjnqtxavxtwvforuhgpowofwyxtlmujnteinaitdxrpyjeklyqohxxfibvdarfjffrprrrqrhbglpihlgshmnubdsfnqchxctdxiqejoulzzudmipwkmrgylufdfifosyrrgchoofqvevxlnjxibfdfrazvwdnefguomsmmlcdbyputygmsgzsnbagktwokdsrowrdxbvjbglffsxnqkfktiqqigvuexjsdyzdoysswwykbkatlcuoqbpqsgiloxxtrynkgwgvwqvcphrrwwgbmrzrfexbcadtckgzkupwrhtogzhlpmzofvaugqckkkkmfxogdmqhcnblieofbjgzmxitfhwsvdxxjacenozyv")
