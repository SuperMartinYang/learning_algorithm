string = """a.dozac  fvh2bv7!iKP&..Ape>X6UYvk
a.jeel   R~nngw}Po2f^JA}3vKnbeX6&
a.thompson Ubf=rbEq3fkUNW+-LG9L_M>K
b.cakely	4rPRu=wv_8G>BDk@&Ep!,a?q
b.wells		Neetd)Np*@Myc&?#-ua-v@gD
c.wheeler	9wsNc=fzcRsU.4H4Bf:jrPUZ
c.licht		Ee^Z=D6F.k84tj8,AY_Dg&LE
d.brady		h&gvY!H.},^H4uVL8eG_drjk
f.castle	cd]P,U@*!Jwr8>b.Nud*CA@B
h.peterson	PKK_jbg#JA8Zn&PLosfymfu)
j.hoyt		#yN.haP=f-i4!:qi,C,:Mjb-
j.wright	Z>>ukyRo}8X3Xe^+-MYnm^Fr
j.bowler	h&+RX6PWmVV-9ZJkrGB3mt?6
j.bile		qoA_*AUg.C.QvVRVFkP}.t##
k.holmes	bT}>~QyWyn,:r?@z)#4#FFoo
l.delrose	UQkwHE7W.Tc_fcmUoq]fCM*P
m.haynes	,zrdNniJRJqrkon~V)XQnxzz
n.kevans	VB?V8M?tf,KpifGFU^iw%7U)
p.emerson	p6tq.2=d8fgx3:>TBRTC4u7q
p.luther2	Ebii8DkW#Z-Gr^8mJeQhpYH&
p.luther	*F=pT#M>W%YbCRiBn!_T8@@@
r.variable	^7g>Zrrn8ALo}z]b.Eh}K}vJ
s.wilhelm	Mn),oR*h@YJRWqj#nbAkx_qE
s.harlem	AUa&EQBF.8zvyvzWVy~U2b=^
s.bott		U&xQrkm7d4L!X]Ahiib!^xRN
s.smith		Xx9%dHMt3QYuefo2Gv}Y&dBq
s.jobs		uC&jXuJX9s}p.}8%a%bJ3G2r
s.taylor	YeHF_X:K4h8HxAec9z.Uv87Q
t.fritz		YE-Z9A3enD&>z3R,fU)Ay3bc"""
# up = string.split("\n")
# dealup = [i.split() for i in up]
# res = ""
# for item in dealup:
    # res += "sudo mkdir /var/www/%s\n" % item[0]
    # res += "sudo chmod 555 /var/www/%s\n" % item[0]
    # res += "%s\n%s\n" % (item[0], item[1])
#     res += "sudo adduser --disabled-password --gecos \"\" --force-badname \"%s\"\n" % item[0]
#     res += "sudo echo -e \'%s\\n%s\\n\' | passwd \"%s\"\n" % (item[1], item[1], item[0])
#     res += "sudo echo -e \'%s\\n%s\\n\' | sudo htpasswd -mi /etc/vsftpd/ftpd.passwd \"%s\"\n" % (item[1], item[1], item[0])
#     res += "sudo chown root:root /home/%s\n" % item[0]
#     res += "sudo mkdir /home/%s/files\n" % item[0]
#     res += "sudo chown %s:%s /home/%s/files\n" % (item[0], item[0], item[0])
# print(res)
# with open("add.sh", 'a') as addshell:
#     addshell.write(res)
import sys
for i in sys.stdin:
    print(i)
