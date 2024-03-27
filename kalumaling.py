
        global lima
        global j
        global k
        global laco
        global jud
        global stas
        if "Kamu berhasil mencuri" in event.raw_text:
            j +=1
            k +=1
            time.sleep(1)
            if k%2 == 0:
                await clien.send_message(random.choice(mepa), "1")
                return
            else:
                await clien.send_message(random.choice(mepa), lima[j])
                return
            #await clien.send_message(random.choice(mepa), "1")
            return
        
        if "tidak bisa dirampok" in event.raw_text:
            j +=1
            time.sleep(1)
            await clien.send_message(random.choice(mepa), lima[j])
            return
        
        if "memenjarakanmu" in event.raw_text:
            time.sleep(int(re.findall(r'\w+', event.raw_text)[-2])*60)
            await clien.send_message(random.choice(mepa), lima[j])
            return
        
        if "tidak punya barang" in event.raw_text:
            #print(lima[j])
            j +=1
            time.sleep(1)
            await clien.send_message(random.choice(mepa), lima[j])
            return
        
        if "Keamanan rumah" in event.raw_text:
            j +=1
            time.sleep(1)
            await clien.send_message(random.choice(mepa), lima[j])
            return
        
        if "menghilang dari peradaban" in event.raw_text:
            print(lima[j])
            j +=1
            time.sleep(1)
            await clien.send_message(random.choice(mepa), lima[j])
            return
        
        if "petani baik lagi" in event.raw_text:
            time.sleep(2)
            if time.time()-jud >= 240:
                await clien.send_message(random.choice(mepa), "/casino_hasil")
                return
            else:
                await clien.send_message(random.choice(mepa), lima[j])
                return
            return

        if "cukup energi untuk" in event.raw_text:
            time.sleep(2)
            await clien.send_message(random.choice(mepa), "/makan_SteakKambingKeramat")
            return
        
        if 'kamu tidak bisa makan' in event.raw_text:
            antos = (60-int(event.raw_text.split( )[19]))*60
            time.sleep(antos)
            await clien.send_message(random.choice(mepa), "/makan_SteakKambingKeramat")
            return
        
        if 'Energi berhasil' in event.raw_text:
            #antos = (60-int(event.raw_text.split( )[19]))*60
            #time.sleep(antos)
            time.sleep(1)
            await clien.send_message(random.choice(mepa), lima[j])
            return
        
        if 'Pasar Khusus' in event.raw_text:
            #antos = (60-int(event.raw_text.split( )[19]))*60
            #time.sleep(antos)
            time.sleep(2)
            await clien.send_message(random.choice(mepa), lima[j])
            return
        
        if 'Uuuh rasanya' in event.raw_text:
            time.sleep(1)
            await clien.send_message(random.choice(mepa), '1')
            time.sleep(1)
            await clien.disconnect()
            return

        if 'Berhasil bertaruh' in event.raw_text:
            jud = time.time()
            time.sleep(1)
            await clien.send_message(random.choice(mepa), lima[j])
            return
        
        if 'Kamu bertaruh' in event.raw_text:
            mas = 0
            time.sleep(1)
            if time.time()-stas < 1200:
                await clien.send_message(random.choice(mepa), "/casino_FiftyFifty_"+str(random.randint(1,2))+"_5000000000")
                return
            else:
                await clien.send_message(random.choice(mepa), "/status")
                return
            return
        
        if 'Online' in event.raw_text:
            stas = time.time()
            time.sleep(1)
            #await clien.send_message('KampungMaifamA4bot', '/prlt_CariRumput')
            await clien.send_message(random.choice(mepa), "/casino_FiftyFifty_"+str(random.randint(1,2))+"_5000000000")
            return
        
        if 'keamanan kembali' in event.raw_text:
            stas = time.time()
            time.sleep(1)
            #await clien.send_message('KampungMaifamA4bot', '/prlt_CariRumput')
            await clien.send_message(random.choice(mepa), "/casino_FiftyFifty_"+str(random.randint(1,2))+"_5000000000")
            return
        
        if 'Offline' in event.raw_text:
            time.sleep(1)
            await clien.send_message(random.choice(mepa), "/aktifkan_sekarang")
            return
        
        if 'Target EXP tercapai' in event.raw_text:
            #print(ter)
            time.sleep(1)
            await clien.send_message(random.choice(mepa), "/casino_FiftyFifty_"+str(random.randint(1,2))+"_5000000000")
            #laco = "/water"
            #print(ter)
            return
        
        if 'Selesaikan' in event.raw_text:
            time.sleep(1)
            await clien.send_message(random.choice(mepa), "/casino_hasil")
            #print('eh acan anggeus')
            return
        
        if 'akan keluar' in event.raw_text:
            time.sleep(int(event.raw_text.split( )[3]))
            await clien.send_message(random.choice(mepa), "/casino_hasil")
            return
        
        if 'Belum ada taruhan' in event.raw_text:
            time.sleep(1)
            await clien.send_message(random.choice(mepa), "/casino_FiftyFifty_"+str(random.randint(1,2))+"_5000000000")
            #print('Judi Lagi')
            return
 