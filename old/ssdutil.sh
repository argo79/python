# verifica jouyrnaling: tune2fs -O ^has_journal /dev/sdXY 

mount /dev/sdXY /mnt

# nel file /mnt/etc/default/grub aggiungere dopo quiet spalsh:
# rootfstype=ext4 elevator=noop

poi montare le partizioni utili a montare il sistema:

mount --bind /dev /mnt/dev
mount --bind /proc /mnt/proc
mount --bond /sys /mnt/sys

# cambiare quindi utente e sistema:
chroot /mnt
update-grub2
exit

umount /mnt/dev
umount /mnt/proc
umount /mnt/sys
umount /mnt/

#riavviare il sistema
# riverificare con dumpe2fs -h /dev/sdXY
