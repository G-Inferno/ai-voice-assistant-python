import random

quotes = {
    1: "Life is about making an impact, not making an income. --Kevin Kruse",
    2: "Whatever the mind of man can conceive and believe, it can achieve. –Napoleon Hill",
    3: "Strive not to be a success, but rather to be of value. –Albert Einstein",
    4: "Two roads diverged in a wood, and I—I took the one less travelled by, And that has made all the difference. –Robert Frost",
    5: "I attribute my success to this: I never gave or took any excuse. –Florence Nightingale",
    6: "You miss 100% of the shots you don’t take. –Wayne Gretzky",
    7: "I've missed more than 9000 shots in my career. I've lost almost 300 games. 26 times I've been trusted to take the game winning shot and missed. I've failed over and over and over again in my life. And that is why I succeed. –Michael Jordan",
    8: "The most difficult thing is the decision to act, the rest is merely tenacity. –Amelia Earhart",
    9: "Every strike brings me closer to the next home run. –Babe Ruth",
    10: "Definiteness of purpose is the starting point of all achievement. –W. Clement Stone",
    11: "Life isn't about getting and having, it's about giving and being. –Kevin Kruse",
    12: "Life is what happens to you while you’re busy making other plans. –John Lennon",
    13: "We become what we think about. –Earl Nightingale",
    14: "Twenty years from now you will be more disappointed by the things that you didn’t do than by the ones you did do, so throw off the bowlines, sail away from safe harbor, catch the trade winds in your sails. Explore, Dream, Discover. –Mark Twain",
    15: "Life is 10% what happens to me and 90% of how I react to it. –Charles Swindoll",
    16: "The most common way people give up their power is by thinking they don’t have any. –Alice Walker",
    17: "The mind is everything. What you think you become. –Buddha",
    18: "The best time to plant a tree was 20 years ago. The second best time is now. –Chinese Proverb",
    19: "An unexamined life is not worth living. –Socrates",
    20: "Eighty percent of success is showing up. –Woody Allen",
    21: "Your time is limited, so don’t waste it living someone else’s life. –Steve Jobs",
    22: "Winning isn’t everything, but wanting to win is. –Vince Lombardi",
    23: "I am not a product of my circumstances. I am a product of my decisions. –Stephen Covey",
    24: "Every child is an artist. The problem is how to remain an artist once he grows up. –Pablo Picasso",
    25: "You can never cross the ocean until you have the courage to lose sight of the shore. –Christopher Columbus",
    26: "I’ve learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel. –Maya Angelou",
    27: "Either you run the day, or the day runs you. –Jim Rohn",
    28: "Whether you think you can or you think you can’t, you’re right. –Henry Ford",
    29: "The two most important days in your life are the day you are born and the day you find out why. –Mark Twain",
    30: "Whatever you can do, or dream you can, begin it. Boldness has genius, power and magic in it. –Johann Wolfgang von Goethe",
    31: "The best revenge is massive success. –Frank Sinatra",
    32: "People often say that motivation doesn’t last. Well, neither does bathing. That’s why we recommend it daily. –Zig Ziglar",
    33: "Life shrinks or expands in proportion to one's courage. –Anais Nin",
    34: "If you hear a voice within you say 'you cannot paint,' then by all means paint and that voice will be silenced. –Vincent Van Gogh",
    35: "There is only one way to avoid criticism: do nothing, say nothing, and be nothing. –Aristotle",
    36: "Ask and it will be given to you; search, and you will find; knock and the door will be opened for you. –Jesus",
    37: "The only person you are destined to become is the person you decide to be. –Ralph Waldo Emerson",
    38: "Go confidently in the direction of your dreams. Live the life you have imagined. –Henry David Thoreau",
    39: "When I stand before God at the end of my life, I would hope that I would not have a single bit of talent left and could say, I used everything you gave me. –Erma Bombeck",
    40: "Few things can help an individual more than to place responsibility on him, and to let him know that you trust him. –Booker T. Washington",
    41: "Certain things catch your eye, but pursue only those that capture the heart. –Ancient Indian Proverb",
    42: "Believe you can and you’re halfway there. –Theodore Roosevelt",
    43: "Everything you’ve ever wanted is on the other side of fear. –George Addair",
    44: "We can easily forgive a child who is afraid of the dark; the real tragedy of life is when men are afraid of the light. –Plato",
    45: "Teach thy tongue to say, 'I do not know,' and thou shalt progress. –Maimonides",
    46: "Start where you are. Use what you have. Do what you can. –Arthur Ashe",
    47: "When I was 5 years old, my mother always told me that happiness was the key to life. When I went to school, they asked me what I wanted to be when I grew up. I wrote down 'happy'. They told me I didn’t understand the assignment, and I told them they didn’t understand life. –John Lennon",
    48: "Fall seven times and stand up eight. –Japanese Proverb",
    49: "When one door of happiness closes, another opens, but often we look so long at the closed door that we do not see the one that has been opened for us. –Helen Keller",
    50: "Everything has beauty, but not everyone can see. –Confucius",
    51: "How wonderful it is that nobody need wait a single moment before starting to improve the world. –Anne Frank",
    52: "When I let go of what I am, I become what I might be. –Lao Tzu",
    53: "Life is not measured by the number of breaths we take, but by the moments that take our breath away. –Maya Angelou",
    54: "Happiness is not something readymade. It comes from your own actions. –Dalai Lama",
    55: "If you're offered a seat on a rocket ship, don't ask what seat! Just get on. –Sheryl Sandberg",
    56: "First, have a definite, clear practical ideal; a goal, an objective. Second, have the necessary means to achieve your ends; wisdom, money, materials, and methods. Third, adjust all your means to that end. –Aristotle",
    57: "If the wind will not serve, take to the oars. –Latin Proverb",
    58: "You can’t fall if you don’t climb. But there’s no joy in living your whole life on the ground. –Unknown",
    59: "We must believe that we are gifted for something, and that this thing, at whatever cost, must be attained. –Marie Curie",
    60: "Too many of us are not living our dreams because we are living our fears. –Les Brown",
    61: "Challenges are what make life interesting and overcoming them is what makes life meaningful. –Joshua J. Marine",
    62: "If you want to lift yourself up, lift up someone else. –Booker T. Washington",
    63: "I have been impressed with the urgency of doing. Knowing is not enough; we must apply. Being willing is not enough; we must do. –Leonardo da Vinci",
    64: "Limitations live only in our minds. But if we use our imaginations, our possibilities become limitless. –Jamie Paolinetti",
    65: "You take your life in your own hands, and what happens? A terrible thing, no one to blame. –Erica Jong",
    66: "What’s money? A man is a success if he gets up in the morning and goes to bed at night and in between does what he wants to do. –Bob Dylan",
    67: "I didn’t fail the test. I just found 100 ways to do it wrong. –Benjamin Franklin",
    68: "In order to succeed, your desire for success should be greater than your fear of failure.",
    69: "A person who never made a mistake never tried anything new. –Albert Einstein",
    70: "The person who says it cannot be done should not interrupt the person who is doing it. –Chinese Proverb",
    71: "There are no traffic jams along the extra mile. –Roger Staubach",
    72: "It is never too late to be what you might have been. –George Eliot",
    73: "You become what you believe. –Oprah Winfrey",
    74: "I would rather die of passion than of boredom. –Vincent van Gogh",
    75: "A truly rich man is one whose children run into his arms when his hands are empty. –Unknown",
    76: "It is not what you do for your children, but what you have taught them to do for themselves, that will make them successful human beings. –Ann Landers",
    77: "If you want your children to turn out well, spend twice as much time with them, and half as much money. –Abigail Van Buren",
    78: "Build your own dreams, or someone else will hire you to build theirs. –Farrah Gray",
    79: "The battles that count aren't the ones for gold medals. The struggles within yourself—the invisible battles inside all of us—that's where it's at. –Jesse Owens",
    80: "Education costs money. But then so does ignorance. –Sir Claus Moser",
    81: "I have learned over the years that when one's mind is made up, this diminishes fear. –Rosa Parks",
    82: "It does not matter how slowly you go as long as you do not stop. –Confucius",
    83: "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. –Oprah Winfrey",
    84: "Remember that not getting what you want is sometimes a wonderful stroke of luck. –Dalai Lama",
    85: "You can’t use up creativity. The more you use, the more you have. –Maya Angelou",
    86: "Dream big and dare to fail. –Norman Vaughan",
    87: "Our lives begin to end the day we become silent about things that matter. –Martin Luther King Jr.",
    88: "Do what you can, where you are, with what you have. –Teddy Roosevelt",
    89: "If you do what you’ve always done, you’ll get what you’ve always gotten. –Tony Robbins",
    90: "Dreaming, after all, is a form of planning. –Gloria Steinem",
    91: "It's your place in the world; it's your life. Go on and do all you can with it, and make it the life you want to live. –Mae Jemison",
    92: "You may be disappointed if you fail, but you are doomed if you don't try. –Beverly Sills",
    93: "Remember no one can make you feel inferior without your consent. –Eleanor Roosevelt",
    94: "Life is what we make it, always has been, always will be. –Grandma Moses",
    95: "The question isn’t who is going to let me; it’s who is going to stop me. –Ayn Rand",
    96: "When everything seems to be going against you, remember that the airplane takes off against the wind, not with it. –Henry Ford",
    97: "It’s not the years in your life that count. It’s the life in your years. –Abraham Lincoln",
    98: "Change your thoughts and you change your world. –Norman Vincent Peale",
    99: "Either write something worth reading or do something worth writing. –Benjamin Franklin",
    100: "Nothing is impossible, the word itself says, 'I’m possible!' –Audrey Hepburn",
    101: "The only way to do great work is to love what you do. –Steve Jobs",
    102: "If you can dream it, you can achieve it. –Zig Ziglar",
    103: "Success is not the key to happiness. Happiness is the key to success. – Albert Schweitzer",
    102: "Don’t wait. The time will never be just right. – Napoleon Hill",
    103: "The only way to do great work is to love what you do. – Steve Jobs",
    104: "Act as if what you do makes a difference. It does. – William James",
    105: "Life is what happens when you’re busy making other plans. – John Lennon",
    106: "It always seems impossible until it’s done. – Nelson Mandela",
    107: "Keep smiling, because life is a beautiful thing and there’s so much to smile about. – Marilyn Monroe",
    108: "The harder the conflict, the greater the triumph. – George Washington",
    109: "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    110: "In the middle of every difficulty lies opportunity. – Albert Einstein",
}

def get_random_quote():
    quote_id = random.choice(list(quotes.keys()))
    return quotes[quote_id]