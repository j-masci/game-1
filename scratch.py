
# thrust....
# it attempts to move the velocity
# but doesnt it also attempt to modify acceleration?
# is acceleration some vector we could store on an entity?
# or is acceleration implied from the difference in speed
# from one frame to the next.
# maybe thrust is more like constant acceleration but subject to
# possibly become lower once reaching a certain velocity, due to friction
# or air resistance or w/e.
# i just dont know if we need pos, vel, and accel or just pos and vel? or
# just pos? if pos, vel, and accel, why wouldn't we also have flux?
# in reality things really only do have positions but if we wanted
# to make something change position at constant speed it would only
# be natural to just store a velocity vector and apply it each iteration.
# ok so if we want to change velocity then what...


class Test(int):
    pass
