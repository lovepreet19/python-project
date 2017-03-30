print ('enter 1 for students_to_teacher')
print ('enter 2 for battleship')
print ('enter 3 for exam_stats')

ch = input("enter choice")
if ch=="1":
    import students_to_teacher
    students_to_teacher.students_main()
elif ch=="2":
    import battleship
    battleship.battleship()
elif ch=="3":
    import exam_stats
    exam_stats.exam_stats_main()
else:
    print("wrong entry")
