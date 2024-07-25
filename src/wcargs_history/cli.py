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
        # TODO 명령어 카운트
    elif args.top:
        print(f"-t => {args.top}")
        if args.dt:
            print(f"-d => {args.dt}")
            # TODO 특정 날짜의 명령어 TOP N
        else:
            print("TODO - 에러나 안내 메세지를 출력")
    else:
        # TODO - 사용법을 출력한다.
        parser.print_help()

    if True:
        print("verbose ON")
    else:
        print("verbose OFF")
    

