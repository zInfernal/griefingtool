B
    ¾ÊÎ_¼!  ã            °  @   s  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlm	Z	m
Z
 d dlm	Z	mZm
Z
 d dlZd dlT d dlZd dlZd dlmZmZ d dlZdd Zdd	 Zd
d Zx¾e  e  ee	j de	j Zedkrþe  e  e ¡ Zee	j de	j Zee	j de	j Zee	j de	j ZeeZeeZe d e  e  dd Z!dd Z"e# Z$x,e%dD ] Z&ej'e"dZ(de(_)e( *¡  qW xe%eeD ]Z+e$ ,e+¡ qÆW e$ -¡  e d ee	j. d nedkre  e  dddddd d!d"d#d$d%d&d'd(d)d*d+d,d-d.d/d0d1d2d3d4d5d6d7d8d9d:d;d<d=d>d?d@dAdBdCdDdEdFdGdHdId;dJdKdLdMdNdOdPdQdRdSdTdUdVdWdXdYdZd[d\d]d^d_d`dadadbdcdddedfdgdhdidjdkdldmdndodpdqdrdsdtdudvdwdrdxdydzd{drd|d}d~dddddddddddddddddddddddddddddddddd d¡d¢d£d:d¤d¥d¦d§d¨d©dªd«d¬d­d®d¯d°d±d²d³d´dµd¶d·d¸d¹dºd»d¼d½d¾d¿dÀdÁdÂdÃdÄdÅdÆd½dÇdÈdÉdÊdËdÌdÍdÎdÏdÐdÑdÒdÓdÔdÕdÖd×dØdÙdÚdÛdÜdÝdÞdßdàdádâdãdädådXdYdZd[d\d]d^d_d`dadadbdcdddedfdgdhdidjdkdldmdndodpdqdrdsdtdudvdwdrdxdydzd{drd|ddddddddddddddddddddddddddd¢dæd£d:dçdèdédêdëdìdídîdïdðdñdòdódôdõdöd÷dødùdúdûdüdýdþdÿd(d'd ddddddddd	d
ddddxddddddddddddddddddddddd d!d"d#d$d%d&dVd'd(d)d*d+d,d-d.dd/d0d1d2d3d4d5d6dÌd7d8d9d:d;d<d=d>d?d¢d@dAdBdCdDdEdFddGdHdIdJdKdLdMdddþdÿdNdOdPdQdRddSdTdUdVdWdXdYdZd[d\d]d^d£d_d«d`dadbdcdddedfdgd¿dhdid¼dg°Z/ee	j dje	j Z0e0 1¡ Z2e  e  e d xâe/D ]ÚZ3yÆe4e3dk e4e2 Z5e  6e4e5¡Z7e7 8dl¡re e	j9 dme	j e4e3 dke4e2 dne	j doe4e7 dpe	j. dq n>e e	j9 dme	j e4e3 dke4e2 dne	j e4e7 	 W n   Y nX qW e d ee	j. d qÐW dS (r  é    N)ÚForeÚStyle)r   ÚBackr   )Ú*)ÚchoiceÚ	randrangec              C   s   t  d¡} d S )Nzcls || clear)ÚosÚsystem)Úclear© r   ú(/home/zinfernal123/griefing-tool/tool.pyr
      s    r
   c               C   s   t tj d d S )Nu  


ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ

	)Úprintr   ÚLIGHTRED_EXr   r   r   r   Úbanner   s    
r   c            $   C   s¢   t   t  tdtj dtj dtj dtj dtj dtj dtj dtj dtj d	tj dtj d
tj dtj dtj dtj dtj dtj d# d S )NÚ
z& ____________________________________
z'|                                    |
z| z(1) zPortScanner      ú|z    BYz     |
z(2) zSubdomainScanner z zInfernal z|
z+|____________________________________|
	

	)r
   r   r   r   ÚLIGHTCYAN_EXr   r   r   r   r   Úmenu!   s    r   z>>] Ú1z|IP] >> z|StartPort] >> z|EndPort] >> r   c          	   C   sl   t   t jt j¡}yJ| t| f¡}t& ttj dtj	 t d|   W d Q R X | 
¡  W n   Y nX d S )Nz	OPEN] >> ú:)ÚsocketZAF_INETZSOCK_STREAMZconnectÚtargetÚ
print_lockr   r   ÚLIGHTGREEN_EXr   Úclose)ÚportÚsZconr   r   r   Úportscan>   s    *r   c              C   s"   xt  ¡ } t|  t  ¡  qW d S )N)ÚqÚgetr   Z	task_done)Úworkerr   r   r   ÚthreaderH   s    r!   iô  )r   Tz> Presiona EnterÚ2ÚallZnetZbypassZrconZnode010Znode09Znode08Znode07Znode06Znode05Znode04Znode03Znode02Znode01ZsupremeZ	subnormalZfunZaaaZaaÚaZkiwiZserver10Zserver09Zserver08Zserver07Zserver06Zserver05Zserver04Zserver03Zserver02Zserver01ZdevZ	recuperarZdedisZdedicadoZvoteZeventsZwwwz
ovh-birdmcZcpanelzns-vpsÚdÚtZshortZjarZiptablesZufwZbaneadosZimagenesZsampZsocialZholoZ
donacionesZshoprpZwowZ
multicraftZmailZradio3Zradio2ZfrZteamdubZserieytZshopZreportZapplyZyoutubeZtwitterÚstZlostZsgZsrvc1ZtorneoZserv11Zserv0Zserv10Zserv9Zserv7Zserv6Zserv5Zserv4Zserv3Zserv2Zserv1ZservZmcpZpaysafeZmuZradioZdonateZvps03Zvps02Zvps01ZxenonZbansZns2Zns1ZdonarÚnewZappealsZreportsZtranslationsZ	marketingZstaffZbugsÚhelpZrenderZforoZts3ZgitZ	analyticsZcoinsZvotoszdocker-mainZdockerÚmainZserver3ZcdnZserver2ZcreativoZyt2ZytZfactionsZsolderZtest1Ztest001ZtestpeneZtestZpanelZapoloZsv3Zsv2Zsv1ZbackupsZzeusZthorZvpsZwebZtvZdepositoZ	depositosZextraZextrasZbungee1ZtorneoytZhcfZuhc5Zuhc4Zuhc3Zuhc2Zuhc1ÚuhcZ	dedicado5Z	dedicado4Z	dedicado3Z	dedicado2Zded5Zded4Zded3Zded2Zded1ZdedZgamehitodrhZ	servidor4ZwebmailZmonitorZservidor001Z
servidor10Z	servidor9Z	servidor8Z	servidor7Z	servidor6Z	servidor5Z	servidor3Zhvokfcic7smZautodiscoverZtauchetZhg10ZpingZhg9Zhg8Zhg7Zhg6Zhg5Zhg4Zhg3Zhg2Zhg1ZtiendaZstatusZayudaZplaystationÚhomeZjobZfirewallZrankZmantenimientoZbetaZpayZprivater   ZbbZstorZmx5ZbuildZmcZplayÚsysZnode1Znode2Znode3Znode4Znode5Znode6Znode7Znode8Znode9Znode10Znode11Znode12Znode13Znode14Znode15Znode16Znode17Znode18Znode19Znode20Znode001Znode002Znode003Zsys001Zsys002ZgoZadminZeggwarsZbedwarsZlobby1ZhubZbuilderZ	developerZforumZbaneosZtsZsys1Zsys2ZmodsZbungeeZ
bungeecordZarrayZspawnZserverZclientZapiZsmtpÚs1Ús2Zs3Zs4Zserver1ZjugarZloginZmysqlZ
phpmyadminZdemoZnaZeuÚusZesÚitZruZsupportZ
developingZdiscordZbackupZbuyZbuycraftZ	dedicado1ZdediZdedi1Zdedi2Zdedi3Z	minecraftZpruebaZpruebasÚregisterZstatsZstoreZserieZ	buildteamÚinfoZhostZjogarÚproxyZovhZpartnerZpartnersZappealzstore-assetsZbuildsZtestingZpvpZskywarsZsurvivalZskyblockZlobbyZhgZgamesZgames001Zgames002Zgame001Zgame002Zgame003Zus72Zus1Zus2Zus3Zus4Zus5Z
goliathdevZstaticassetsZrewardsZrpsrvZftpZsshZjobsZgrafanaZvote2ÚfileZsentryZenjinZ	webserverZxenZmcoZ	servidor2Zsadrez|Domain] >> Ú.z104.z|Subdominio] >> z >> ú(z) z(CloudFlare)):r   Ztimer-   r   ZcoloramaÚ
subprocessZrequestsÚbase64Z	threadingr   r   r   ZqueueZargparseZrandomr   r   r
   r   r   Úinputr   ZWHITEZmenu_opcionesZLockr   r   Zport1Zport2ÚintZ	startportZendportr   r   r!   ZQueuer   ÚrangeÚxZThreadr&   ZdaemonÚstartr    ZputÚjoinr   Zsubdomains0ZxyÚlowerZxyyZ	ejecutar0ÚstrZ	ipserver0ZgethostbynameZiphost0Ú
startswithr   r   r   r   r   Ú<module>   s~   X


ÿ ÿ ÿ ÿ J
RB