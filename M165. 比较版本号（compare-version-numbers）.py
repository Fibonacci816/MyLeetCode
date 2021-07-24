class Solution:
    # 时间O(max(m,n)) 空间O(m+n)
    def compareVersion(self, version1: str, version2: str) -> int:
        # 以.分割版本号
        def get_split_version(version):
            version_split = version.split('.')
            return [int(v) for v in version_split]
        # 比较分割后的版本号
        def compare_split_version(version1_split, version2_split):
            n1, n2 = len(version1_split), len(version2_split)
            for i in range(max(n1, n2)):
                split1 = version1_split[i] if i < n1 else 0
                split2 = version2_split[i] if i < n2 else 0
                if split1 > split2:
                    return 1
                elif split1 < split2:
                    return -1
            return 0
        version1_split = get_split_version(version1)
        version2_split = get_split_version(version2)
        return compare_split_version(version1_split, version2_split)