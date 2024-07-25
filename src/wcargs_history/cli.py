import argparse



def hello_wcargs():
    return "hello"

def cmd():
    msg = hello_wcargs()
    #print(msg)

    parser = argparse.ArgumentParser(
            prog='ProgramName',
            description=' ',
            epilog=' '
            )
    parser.add_argument('-s', '--scount')
    parser.add_argument('-d', '--dt')
    parser.add_argument('-t', '--top')


    args = parser.parse_args()
    print(args.scount, args.top, args.dt)
    
    if args.scount:
        print(f"-s => {args.scount}")
    elif args.top:
        print(f"-t => {args.top}")
        if args.dt:
            print(f"-d => {args.dt}")
        else:
            print(" TODO")


    if True:
        print("verbose ON")
    else:
        print("verbose OFF")
    

