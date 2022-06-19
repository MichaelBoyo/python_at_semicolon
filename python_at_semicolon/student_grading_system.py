import ab
no_subs, no_studs = int(input("enter number of subjects: ")), int(input("enter number of students: "))
print()
subs, db, t, a, p = [input(f"enter sub {i} name: ") for i in range(1, no_subs + 1)], [], "Tot", "Avg", ""
print()
for a in range(1, no_studs + 1):
    name = input("enter student name: ")
    sub_scs = [int(input(f"enter {name} score for {sub_name}: ")) for sub_name in subs]
    tot = sum(sub_scs)
    avg = tot / len(subs)
    data = {"student name": name, "sub scores": sub_scs, "total score": tot, "average score": avg}
    db.append(data), print()
avg_scs, std_n = [int(n["average score"]) for n in db], [n["student name"] for n in db]
t_scs, scs = [int(n["total score"]) for n in db], [n["sub scores"] for n in db]
print("=" * 46, "\n", "Welcome to Semicolon School Grading System", "\n", "=" * 46, "\n", "Native", end=" ")
for a in subs:
    print(f"{a:>7}", end=" ")
print(f"{t:>7}{a:>7}{p:>7}")
for i in range(0, len(db)):
    print(f"{std_n[i]}", end=""), ab.ret(scs[i]), print(f"{t_scs[i]:>8}{avg_scs[i]:>7}")
print("=" * 46)
