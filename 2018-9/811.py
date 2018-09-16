# -*- coding: utf-8 -*-
# @Time    : 2018/9/16 下午6:32
# @Author  : jaelyn
# @FileName: 811.py
# @Software: PyCharm

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        ret_dic = {}
        for domain in cpdomains:
            num, str_domain = str(domain).split(' ')
            ret_dic.update({str_domain: ret_dic.get(str_domain, 0)+int(num)})
            while str(str_domain).find('.') != -1:
                str_domain = str_domain[str(str_domain).find('.')+1:]
                ret_dic.update({str_domain: ret_dic.get(str_domain, 0) + int(num)})
        ret_list = []
        for key, value in ret_dic.items():
            ret_list.append(str(value)+" "+key)
        return ret_list


if __name__ == '__main__':
    solution = Solution()
    cp = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    ret = solution.subdomainVisits(cp)
    print(ret)