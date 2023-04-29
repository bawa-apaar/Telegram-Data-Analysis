from telethon import TelegramClient, events, sync
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
import io
import json
from datetime import datetime, timedelta
import pytz
utc = pytz.UTC

api_id = #api_id
api_hash = #api_hash

client = TelegramClient('anon', api_id, api_hash)
client.start()

c_name = #channel name
channel_name = client.get_entity(f'https://t.me/{c_name}')

c = client.get_entity(PeerChannel(channel_name.id))
i = 0

msg = {"grouped_id": -1, "message": "",
       "media": {"photos": [],
                 "videos": []},
       "replies_msg": []
       }

check_timestamp = utc.localize(datetime.utcnow()).date() - timedelta(weeks=60)
cur_timestamp = utc.localize(datetime.utcnow()).date()
prev_timestamp = cur_timestamp - timedelta(weeks=1)

json_file = f'{c_name}_{prev_timestamp}_{cur_timestamp}.json'
with open(json_file, 'w', encoding="utf-8") as outfile:
    json.dump({"data": []}, outfile)
outfile = open(json_file, 'r')
all_messages = json.load(outfile)

for m in client.iter_messages(c):
    try:
        if m.action:
            continue

        if cur_timestamp < check_timestamp:
            break

        if prev_timestamp < m.date.date() <= cur_timestamp:
            if m.grouped_id and m.grouped_id != msg["grouped_id"]:
                if msg["grouped_id"] != -1:
                    all_messages["data"].append(msg)
                    write_json_file = open(json_file, 'w', encoding="utf-8")
                    json.dump(all_messages, write_json_file, ensure_ascii=False)

                msg = {'grouped_id': m.grouped_id, "message": "", "media": {"photos": [], "videos": []}, "replies_msg": []}
                m_id = msg['grouped_id']

            elif m.grouped_id and m.grouped_id == msg["grouped_id"]:
                m_id = msg['grouped_id']

            else:
                if msg != {'grouped_id': -1, "message": "", "media": {"photos": [], "videos": []}, "replies_msg": []}:
                    all_messages["data"].append(msg)
                    write_json_file = open(json_file, 'w', encoding="utf-8")
                    json.dump(all_messages, write_json_file, ensure_ascii=False)

                msg = {'grouped_id': -1, "message": "", "media": {"photos": [], "videos": []}, "replies_msg": []}
                m_id = m.id

            if m.photo:
                print("downloading photo...")
                msg["media"]["photos"].append(f"{m_id}_{m.photo.id}.jpg")
                m.download_media("Dataset/" + str(f"{m_id}_{m.photo.id}.jpg"))

            if m.video:
                print("downloading video...")
                msg["media"]["videos"].append((f"{m_id}_{m.video.id}.mp4", f"{m.video.size * 0.000001:.1f} MB"))
                m.download_media("Dataset/" + str(f"{m_id}_{m.video.id}"))

            if m.message and m.message != '':
                msg['message'] = m.message

            try:
                for r_m in client.iter_messages(c, reply_to=m.id):
                    msg["replies_msg"].append(r_m.message)
            except:
                pass

            if m.reactions:
                msg['reactions'] = {}
                for e in m.reactions.results:
                    msg['reactions'][e.reaction.emoticon] = e.count

            msg["post_id"] = m.id
            msg["post_date"] = m.date.isoformat()
            msg["post_views"] = m.views
            msg["post_forwards"] = m.forwards
            print(f"================================== MSG {i} DONE=================================================")
            i += 1

        else:
            cur_timestamp = m.date.date()
            prev_timestamp = cur_timestamp-timedelta(weeks=1)
            json_file = f'{c_name}_{prev_timestamp}_{cur_timestamp}.json'

            with open(json_file, 'w') as outfile:
                json.dump({"data": []}, outfile)

            outfile = open(json_file, 'r')
            all_messages = json.load(outfile)

    except:
        print(m)

all_messages["data"].append(msg)
write_json_file = open(json_file, 'w', encoding="utf-8")
json.dump(all_messages, write_json_file, ensure_ascii=False)


print("process completed!!")