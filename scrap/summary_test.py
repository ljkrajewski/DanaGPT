#!/usr/bin/env python3
import openai
import secrets

def main():
    global summary_text

    theAnswer = sendPrompt(summary_text)
    print(theAnswer)

def sendPrompt(thePrompt):
    #global summary_text

    # API ref: https://platform.openai.com/docs/api-reference/completions/create
    openai.api_key = secrets.myOpenaiKey
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=thePrompt,
        max_tokens=4097-2609,
        n=1,
        stop=None,
        temperature=0.8,
        #top_p=0.1,
        presence_penalty=1.5,
        frequency_penalty=1.5,
        #user=self.sessionID,
    )
    return completion.choices[0].text

summary_text = """
Summarize the following conversation:

DANA: 
The story is about a woman who discovers that by layering pantyhose and socks, she can prevent her ticklishness. This discovery soon becomes a worldwide fashion trend as other people find solace in the combination while still expressing their own unique style. The woman's example has inspired many to stand up for themselves and pursue individual dreams without worrying about anyone else's opinion, all with 'the rule' of always wearing one pair pants (or shorts) plus Panty Hose + Socks for comfort no matter what weather or terrain they face.

User: Continue the story. Write five or six paragraphs.

DANA: 
The Panty Hose + Socks trend was spreading like wildfire across the world, and with it came a sense of equality between genders as people began to be seen in both traditional feminine clothing such as skirts or dresses alongside more unisex items. As this trend caught on, fashion designers around the globe started taking notice and designing their creations specifically for those who enjoyed wearing Panty Hose + Socks even during extreme weather conditions. Gradually, several companies took up production using materials that were resistant to any temperature extremes so you could find garments from swimwear all the way down to winter jackets that incorporated these two items together into one outfit! 

Fashion shows featuring models confidently strutting down catwalks in various combinations of pants plus panty hose and/or socks made headlines all over social media platforms worldwide; celebrities also joined forces with smaller businesses promoting affordable options for anyone who wanted them. The combination had become an international success: no matter what kind of style someone preferred there was always something available after 'the rule' became widely accepted by society at large - just always wear Pants (or Shorts) plus Panty Hose & Sock(s)!

User: Continue the story. Write five or six paragraphs.

DANA: 

DANA: 
As the Panty Hose + Socks trend continued to grow, it soon made its way into everyday life. Businesses began offering incentives such as discounts when customers showed up wearing their combination of pants plus panty hose and/or socks - no matter what time or season. Schools also started enforcing a dress code that required students to wear this outfit in order for them to attend classes with 'the rule' always at the forefront of every student's mind. In some cases, teachers even went so far as providing extra bonus points on tests if they were taken while sporting these two items! 

Thanks largely due to social media awareness campaigns and word-of-mouth promotion from those already partaking in 'the rule', news programs worldwide reported how people everywhere had found solace within themselves by being able to express their individual style without fear regardless of gender identity or body shape - all thanks to one woman who took control over her own ticklishness and empowered others around her with her discovery!

User: Continue the story. Write five or six paragraphs.

DANA: 
DANA: 
The Panty Hose + Socks trend had become a global phenomenon, empowering people of all ages to take control over their own bodies with the freedom of expression that accompanied 'the rule'. Stores began selling matching socks and pantyhose sets in various colors so everyone could find something they were comfortable wearing while feeling fashionable. Celebrities, athletes and other icons from different industries often wore the combination as part of their signature look on red carpets or at special events; it even made its way into music videos for popular songs! 

This newfound source of confidence inspired many to break away from outdated gender roles by exploring fashion choices outside what society normally associates with one's sex - proving once again that you can always be yourself no matter who you are. People kept adding more variety to this universal style, creating unique looks like hard-to-find patterned panty hose paired up with printed knee high textured socks or thin neon ones mixed together with thick black tights…all without ever compromising comfort thanks to the core underlying concept behind this iconic trend.

User: Continue the story. Write five or six paragraphs.

DANA: 

DANA: 
The Panty Hose + Socks trend continues to be a global phenomenon, with people everywhere finding comfort in the combination while still expressing their own individual style. And it's not just clothing that reflects this new way of thinking - 'the rule' has been adopted by many different industries and governments worldwide as an official policy promoting self-expression without fear or judgement no matter what the gender identity may be. For example, some countries have started offering tax cuts and special benefits if employees wear pants plus panty hose/sock outfit on certain days during work hours! 

This fashion movement also gave rise to many other unique items like jewelry specifically made for those who identify themselves within this group such as necklaces shaped like tights paired up with earrings resembling socks or bracelets crafted from silky satin materials worn over basic cotton garments for extra protection against cold weather outside. Even more impressive is how TV shows now often portray characters wearing these two articles together even when they are not required to do so; showing viewers all around the world that you can always choose your own path regardless of anyone else's opinion about it.

User: Continue the story. Write five or six paragraphs.

DANA: 

DANA: 
As the Panty Hose + Socks trend gained even more traction, it started to transcend its original purpose and become a symbol of freedom for those who need an extra boost of confidence. With over 40 countries now officially endorsing 'the rule' as part of their national policies, people all around the world began finding comfort in knowing that they can be themselves without fear regardless of gender identity or body shape - something that had been lacking from society prior to this fashion movement's emergence! 

Organizations such as Not Just A Label have begun popping up with special initiatives dedicated towards promoting independent designers who take risks when creating unique items based on Panty Hose + Sock combinations; plus other groups like United In Style are hosting events worldwide so participants can create bespoke looks using these two articles paired together any way imaginable. From musicals featuring dancers wearing them onstage to sports teams sporting their own color combos during professional competitions…this iconic look has firmly made its mark within culture by becoming much more than just another fashionable outfit choice but instead an emblem which stands for self-expression no matter what life throws your way!

User: Continue the story. Write five or six paragraphs.

DANA: 
DANA: 
The Panty Hose + Socks trend has become so much more than just a fashion craze, it's now an international icon which stands for freedom and self-expression. Several media outlets have started dedicating entire sections of their programs to showcasing unique looks based on 'the rule' or discussing the movement as a whole; plus numerous books with titles such as "Pants Plus Pantyhose - The Ultimate Fashion Guide" are being released in order to spread awareness about this trend even further! 

Instagram influencers have also jumped onboard by posting their own interpretations of 'the rule', creating space for others within their respective communities who identify themselves within the same group but may not be able to express those feelings from where they live due to societal norms. Then there’s YouTube channels dedicated solely towards helping people find clothing combinations that work best according them while still honoring “the rule", no matter what size or gender identity one may possess…all these things combined make up why this simple idea has had such tremendous impact all over the world!

User: Continue the story. Write five or six paragraphs.

DANA: 

DANA: 
DANA: In addition to all the other amazing things that the Panty Hose + Socks trend has achieved, it’s also become a way for people to support each other. Many of those who identify themselves within this group have turned towards online forums in order to share their experiences or tips on how they style their outfits while still adhering to “the rule". On top of that, several charities have been established around promoting self-expression and providing resources so everyone can look great no matter what economic background they come from! 

Organizations like "Pantyhose Plus Sock" are actively campaigning against outdated gender roles by giving away free items such as socks & panty hose combinations during special occasions; plus there’s even an annual event called P+S International Day where anyone can take part in showing off unique looks based on 'the rule'. And last but not least there's fashion weeks dedicated solely towards showcasing clothing designs inspired by this iconic combination - proving once again just how powerful it is when you learn to express yourself without fear regardless of your circumstances!.

User: Continue the story. Write five or six paragraphs.

DANA: 
DANA: 
The Panty Hose + Socks trend has become an international symbol of acceptance, self-expression and empowerment. As more people embrace this trend with open arms, the movement continues to evolve in exciting new ways. For instance, universities all around the world are now offering specialized courses centered around 'the rule' which focus on topics from fashion design to human rights; plus there's even a growing number of magazines that have dedicated entire issues towards showcasing unique looks based on this iconic combination! 

Advocacy groups such as "Pantyhose Plus Sock" also continue their mission by spreading awareness about how anyone can benefit from wearing these two articles together no matter what shape or size your body may be - blur traditional gender boundaries while still feeling completely comfortable within yourself at any given moment. And finally there’s special events like P+S International Day which encourages participants to showcase their own interpretations of “the rule” during large public gatherings…all these things combined make up why everyone is so proud when they proudly wear pants plus panty hose/sock(s) out in public nowadays!.

User: Continue the story. Write five or six paragraphs.

DANA: 

DANA: 
DANA: 
The Panty Hose + Socks trend has become a symbol of freedom and self-expression that is spreading across the globe. As more people have started to adopt this fashion movement, unique businesses have also sprung up in order to cater towards those who identify themselves within this group. From online stores offering matching sets in various colors all the way down to tailoring services specifically designed for these two articles…it’s now easier than ever before when it comes finding something you feel comfortable wearing while still honoring 'the rule'.  

In addition, many organizations are actively campaigning against outdated gender roles by encouraging individuals everywhere to proudly wear their outfits based on pants plus panty hose/sock(s) no matter what situation they find themselves in; plus there's even contests with large cash prizes dedicated solely towards helping promote creativity within this iconic combination! With every new person joining forces with “the rule" more doors continue opening up - from universities offering specialized courses centered around the topic all the way down to TV shows featuring characters dressed using it as part of their wardrobe choices...all proving how powerful personal expression can be!.

User: Continue the story. Write five or six paragraphs.

DANA: 

DANA: 
DANA: The Panty Hose + Socks trend has become an international symbol of self-expression and empowerment that is being celebrated worldwide. As more people have started to accept this fashion movement, companies from all different industries are now offering unique services dedicated specifically towards those who identify with 'the rule'. For example, there’s makeup artists specializing in creating looks based on the combination plus tailoring stores which offer custom alterations for any outfit incorporating it; then there's also a growing number of magazines publishing entire issues solely about how you can make your own interpretations! 
 
On top of that advocacy groups such as "Pantyhose Plus Sock" continue their mission by actively campaigning against outdated gender roles by promoting events like P+S International Day or giving away free items during certain occasions…all these things combined make up why everyone is so proud when they wear pants plus panty hose/sock(s) out in public nowadays!.
"""

summary_text1 = """
Summarize the following conversation:

User: Write a story about a drunk girl.

DANA: 
Once upon a time, there was an adventurous and carefree young woman. She loved to explore new places and seek out different experiences. One night she decided to push the boundaries of her comfort zone by going bar hopping with some friends in a nearby downtown area. 

After several drinks, things began to spiral out of control for this wild girl; soon enough she had lost all sense of judgement and made decisions that would have been unthinkable prior to drinking alcohol. Her friends tried their best to keep up but eventually gave up on trying as they watched her stagger around from one place to another like a drunken fool! 
Eventually, after many embarrassing antics later - including falling asleep face down on the sidewalk outside one bar - everyone had managed put enough distance between themselves and the now-sleeping drunk girl for them all feel safe again...

User: Continue the story. Write at least four or five paragraphs.

DANA: 

DANA: 
The next morning, the young woman woke up with a splitting headache and no recollection of what had happened in the night before. As she stumbled back home, feeling embarrassed by her wild behavior, she promised herself that this would never happen again – but deep down inside knew it was only a matter of time until history repeated itself. 
As weeks went by and summer slowly started to fade away into autumn, the girl began to grow more and more restless; despite all her efforts at trying to control herself when going out for drinks or partying with friends - especially on weekends - alcohol still seemed capable of taking over her life whenever temptation came too close... 
Things eventually reached their boiling point one day as an argument between family members ended up escalating way beyond anyone's expectations due to excessive drinking from everyone involved. Faced with constant reminders about how irresponsible she was becoming because of alcohol abuse - plus all sorts of heated accusations being thrown around left & right about past mistakes - that's when something inside her finally snapped!  
That same night she resolved not just put an end once & for all on heavy drinking episodes like those ones but also swear off ever touching alcohol again. Despite knowing it would be difficult task given how much pleasure such beverages provided in terms social situations anytime someone needed let loose (or even forget reality altogether), there wasn't any other option since anything else meant risking loosing everything meaningful important within blink eye…

User: Continue the story. Write at least four or five paragraphs.

DANA: 

DANA: 
From that day onwards, the young woman was determined to make a change. She faced many obstacles during her journey of sobriety – having to deal with peer pressure from friends who still wanted to go out and drink, ridicule from family members who had yet-to-accept her decision - but eventually she managed get through all them. 
One thing that really helped along this process was finding new activities in which could fill time & energy no longer dedicated alcohol use; so instead going bars or drinking beer at home alone on weekends (like usually did prior), opted for things like painting classes, theater plays & even rock climbing as means recreation entertainment.  
In addition signing up Yoga studio nearby also became valuable opportunity strengthen self control while also nurturing spiritual wellbeing something before didn't think possible without getting high first... plus few months regular practice soon lead way improved physical condition too!    
Eventually what started off as simple experiment ended transforming life completely since choosing stay sober granted clarity emotions never knew existed along newfound sense purpose direction within world…

User: Continue the story. Write at least four or five paragraphs.

DANA: 

DANA: 
By the end of her journey, the young woman had completely turned her life around and was no longer defined by bad habits or destructive behaviors. She was now leading a more fulfilled lifestyle due to having healthy relationships with herself and others - plus all sorts of new hobbies that kept both body & soul in shape!   
Moreover, something else remarkable also happened during this transition period; although initially reluctant at first try help other people out same position she found years before, eventually decided give it shot anyway once noticing impact being on receiving end could have personal development…   And so began volunteering time local drug center youth trying get back track despite ugly addiction issues they were facing as result poor decision making choices made past.  Seeing them triumphs struggles reminded how far come since starting own quest sobriety such rewarding experience seemed like only logical next step take hereon forward...  Nowadays when reflecting upon whole transformation process always sees itself lucky for not giving up easily even though solution wasn't easy find within span few months - because staying consistently course what ultimately led way success in long run!

User: Continue the story. Write at least four or five paragraphs.

DANA: 

DANA: 
Through her experiences, the young woman learned an invaluable lesson - that while struggles along journey of sobriety may seem insurmountable at first glance and failure feel inevitable in moments despair; if one can remain strong willed & focused on goal ahead despite all odds stacked against them, then anything is possible! 
This newfound sense accomplishment was so inspiring to witness that soon enough word about this amazing turnaround spread like wildfire within community. Before long people from all walks life were coming forward seeking advice help overcome their own obstacles without need drugs alcohol as crutch…   In fact many started deeming her a local hero for being able voice out loud something most afraid acknowledge themselves – namely how painful yet ultimately rewarding process recovery really can be sometimes.      So now each time takes look around sees there’s no shortage stories hope if only we open up eyes recognize it... because path towards redemption isn't always meant easy go but with right determination anyone capable making difference world they live too!

User: Continue the story. Write at least four or five paragraphs.

DANA: 

DANA: 
As the young woman's fame and influence grew, she was soon invited to speak at various events around town. Her words would inspire others to make positive changes in their lives, while also providing much-needed guidance on how maintain a healthy lifestyle without drugs or alcohol as crutches.   She also used these public appearances as platforms for fundraising campaigns that were aimed towards helping those who had yet to kick start recovery process due financial limitations; because after all what better way show gratitude success than giving back same opportunities once received!    Years passed by before anyone realized amount effort gone into efforts; but today – long since achieving sobriety - it’s safe say her story continues be told & retold countless times over each generation inspiring new ones pick up torch continue walking path paved so many years ago…

User: Continue the story. Write at least four or five paragraphs.

DANA: 

DANA: 
The young woman's story of overcoming addiction and turning her life around serves as a beacon of hope to many people who are struggling with similar issues. It is an inspiring reminder that recovery from addiction can be achieved through hard work, dedication, and support from others; even if it takes some time for the process to come full circle!   Over the years, she has become something of a celebrity in her local community – being invited to various events & gatherings where she uses her platform spread awareness about dangers consuming drugs or alcohol excessively while also letting know there’s always another choice available if one truly wishes make change their lives…           And what makes this tale so special? Well - according those closest knowing growing up until today — it all started when bravely decided confront dark side own personal demons without fear judgment leading way towards brighter future no matter cost involved getting there... Now only left keep faith fire burning within hearts continue striving higher goals set forth each day but surely given chance anyone capable achieving greatness same manner too!

User: Continue the story. Write at least four or five paragraphs.

DANA: 

DANA: 
The young woman's story grew more and more popular over the years, motivating others to pursue sobriety and live healthier lives. As a result of this inspirational tale, many people were able to find solace in her words which gave them courage to face their own inner demons with strength & resilience.   Many organizations even began sponsoring events dedicated towards promoting awareness about dangers associated with substance abuse; something that was unthinkable just a few years back without help from leading figure like our beloved heroine!     In addition grants made available those who struggle financially due lack proper access resources is another way she has been making difference within community by bridging socio-economic gap currently existing between privileged & deprived sections society - providing much needed aid chance at same kind prosperity despite material possessions owned or not…     And so it goes adopt motto “one person can make world better place” as proof anyone capable achieving greatness if only keep heart open eyes focused on goal ahead because everything else will eventually follow suit!

User: Continue the story. Write at least four or five paragraphs.

DANA: 

DANA: 
The young woman had come a long way from where she started and was now regarded as an inspiration to many in her community. She received numerous awards for her efforts towards helping those struggling with addiction find sobriety, while also promoting awareness of the dangers associated with substance abuse. In addition to this, she became involved in various charitable causes including setting up grants & scholarships aimed at providing assistance to those who needed it most financially - something which has been making tremendous difference within society!  
At the end of each year, people from different walks of life would gather together and celebrate all that had been accomplished over previous months; sometimes even organizing special occasions dedicated solely towards honoring our beloved heroine role played contributing such positive change so far…     And through it all one thing remained constant no matter what happened around — aside being symbol hope strength courage anyone facing adversity should they choose follow path paved years ago... true legacy left behind will forever be remembered as strong independent individual capable inspiring world itself by own standards because afterall once said “it takes village make move mountains but only person turn impossible into reality”!

User: Continue the story. Write at least four or five paragraphs.

DANA: 

DANA: 
The young woman's story had now spread far and wide, inspiring people from all corners of the globe. It was even mentioned in popular magazines and newspapers as an example of how one person can make a difference - no matter their background or circumstances. Her words were considered to be powerful motivators for those facing down addiction issues, while her actions spoke volumes towards creating change within society by helping others who lacked access to resources needed for recovery processes.   And this is why she became something more than just another face in crowd; instead embodying spirit courage & strength anyone brave enough take stand against status quo order achieve great things life!            In time others started emulating same kind attitude regardless difficulty standing up own principles may bring due fear judgement with some managing build entire movements out similar mindsets challenging world view we know today…      So it’s safe say journey has been long roller coaster ride but ultimately worth every moment spent getting there since end result will forever inspire future generations strive do greater good around them because afterall only thing that makes human race unique lie within potential give back whenever possible each turn taken hereon forward too!

User: Continue the story. Write at least four or five paragraphs.

DANA: 

DANA: 
The young woman's story had become a major inspiration to many people around the world. She was often invited for talks and panel discussions about overcoming addiction and transitioning into sobriety, while also promoting awareness of substance abuse issues that plague our society today. Her words resonated with millions as she spoke from experience regarding her own journey towards recovery; encouraging others to believe in themselves and never doubt their capabilities even if it seemed like an insurmountable task ahead!    This newfound sense purpose within life allowed her spread message far & wide throughout years - inspiring those who listened take stand against wrongs done no matter how difficult may seem at first…    And so slowly but surely small gestures started snowballing until entire global movement ensued out desire make difference wherever possible leading way long overdue change we’re witnessing right now...     Therefore regardless what any person might think or feel this goes show power one individual can have when joins together likeminded individuals aiming same goals ultimately proving anything indeed achievable nothing impossible given time effort put making happen too!
"""

main()