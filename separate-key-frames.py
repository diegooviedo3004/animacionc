from PIL import Image

num_key_frames = 30

with Image.open('video.gif') as im:
	for i in range(im.n_frames):
		im.seek(i)
		im.save('images/{}.png'.format(i))

print(1000/Image.open('video.gif').info["duration"])
