import urllib.request
import re
def report(name):
    def name_to_URL(name):
        if "," in name:
            name1 = name.lower()
            name2=name1.split(',')[::-1]
            name3="-".join(name2)
        else:
            name1=name.lower()
            name3=name1.replace(' ','-')
        return name3


    try:
        # return variable list
        final_job, final_money, final_rank = 0, 0, 0
        new_name=name_to_URL(name)
        page = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/uva2016/'+new_name)
        text1 = page.read().decode('utf-8').strip()
        text = text1.replace('&amp', '&').replace('&lt;', '<').replace('&gt;', '>')

        job=re.compile(r"<span class=\"small text-muted\" id=\"personjob\">([^']+)</span>")
        for m in job.finditer(text):
            final_job=(m.group(1))
        compensation=re.compile(r"<h2 class=\"pay\" id=\"paytotal\">\$([^']+)</h2>")
        for m in compensation.finditer(text):
            compensation2=(m.group(1))
            compensation3=compensation2.replace('$','').replace(',','')
            final_money=float(compensation3)

        #try:

        rank=re.compile(r"University of Virginia rank</td><td>([^ ]+)")
        if not rank.search(text):
            final_rank = 0
        else:
            for m in rank.finditer(text):
                rank1=(m.group(1))
                final_rank=rank1.replace(',','')
        return (final_job, final_money, final_rank)

    except:
        job2=None
        money=0
        rank=0
        return (job2, money, rank)

