import shotgun_api3 as shotgun
from manager.conf import sg_conf as conf

sg = None

def get_sg():

    global sg
    if not sg:
        sg = shotgun.Shotgun(conf.sg_host, conf.sg_log_in[0], conf.sg_log_in[1])
    return sg

if __name__ == "__main__":

    print(get_sg())
    print(get_sg())
