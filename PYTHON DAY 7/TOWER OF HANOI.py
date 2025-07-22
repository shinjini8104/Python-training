def tower(disk, source, auxi, dest):
    if disk == 1:
        print("Move disk 1 from {} to {}".format(source, dest))
        return
    else:
        tower(disk - 1, source, dest, auxi)
        print("Move disk {} from {} to {}".format(disk, source, dest))
        tower(disk - 1, auxi, source, dest)

disk = int(input("Enter number of disks: "))
print("Steps involved are:")
tower(disk, 'A', 'B', 'C')
