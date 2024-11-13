import os
import subprocess



class Common:

    def count_commit():
        return None
        #try:
        #    result = subprocess.run(
        #        ["git", "rev-list", "--count", "HEAD"],
        #        capture_output  =True,
        #        text            =True,
        #        check           =True
        #    )

        #    return result.stdout.strip()

        #except subprocess.CalledProcessError as e:
        #    print(f"Error counting commits: {e}")
        #    return None



    def get_version():
        #return string '666' if commit is None
        commit = Common.count_commit()

        if commit is None:
            return 'Version 666'

        #format commit
        major = 'Version ' + str(os.getenv("VERSION_MAJOR")) + '.'

        if len(commit) > 2:
            return major + commit[:-2] + '.' + commit[-2:]

        elif len(commit) <= 2:
            return major + '0.' + commit

        return major + commit.zfill(2)
