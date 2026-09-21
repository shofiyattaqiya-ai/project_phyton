import random


class AkunTikTok:
    def __init__(self, username, followers):
        self.username = username
        self.followers = followers
    def posting_video(self, judul, is_fyp):
        print(f"🎬 [@{self.username}] upload: '{judul}'")
        if is_fyp:
            self.followers += 5000
            print(f"🔥 FYP Tembus! +5000 Followers. Total: {self.followers}\n")
        else:
            print(f"😢 Sepi penonton.. Total Followers: {self.followers}\n")
    def collab(self, akun_lain):
        print(f"🤝 [@{self.username}] collab bareng [@{akun_lain.username}]!")
        self.followers += 2000
        akun_lain.followers += 2000
        print(f"🎉 Bonus Collab! +2000 Followers untuk kedua akun!\n")

    def live_streaming(self):
        tambah_follower = random.randint(100, 1000)
        self.followers += tambah_follower
        print(f"🔴 [@{self.username}] sedang Live Streaming!")
        print(f"✨ Mendapatkan followers acak sebesar +{tambah_follower}. Total Followers: {self.followers}\n")   

          
user1 = AkunTikTok("kopisenja", 1500)
user2 = AkunTikTok("skibidi_sigma", 800)


user1.posting_video("POV Ngopi pas nnm hujan", is_fyp=False)
user2.posting_video("Tutorial Sigma Male 2026", is_fyp=True)                          

user1.live_streaming()