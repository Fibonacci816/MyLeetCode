class Solution:
    # 哈希表
    # 时间O(n) 空间O(n)
    def numUniqueEmails(self, emails: List[str]) -> int:
        def real_email(email):
            local, domain = email.split('@')
            local = local.replace('.', '')
            local_split = local.split('+')
            return local_split[0] + '@' + domain
        
        return len(set(real_email(email) for email in emails))