def face(color):
    return [[color for _ in range(3)] for _ in range(3)]


class Cube:
    def __init__(self):
        self.uf = face('white')
        self.df = face('yellow')
        self.rf = face('red')
        self.lf = face('orange')
        self.ff = face('green')
        self.bf = face('blue')

    def U(self):
        temp          = self.uf[0][0]
        self.uf[0][0] = self.uf[2][0]
        self.uf[2][0] = self.uf[2][2]
        self.uf[2][2] = self.uf[0][2]
        self.uf[0][2] = temp

        temp          = self.uf[0][1]
        self.uf[0][1] = self.uf[1][0]
        self.uf[1][0] = self.uf[2][1]
        self.uf[2][1] = self.uf[1][2]
        self.uf[1][2] = temp

        temp          = self.bf[0][0]
        self.bf[0][0] = self.lf[0][0]
        self.lf[0][0] = self.ff[0][0]
        self.ff[0][0] = self.rf[0][0]
        self.rf[0][0] = temp

        temp          = self.bf[0][1]
        self.bf[0][1] = self.lf[0][1]
        self.lf[0][1] = self.ff[0][1]
        self.ff[0][1] = self.rf[0][1]
        self.rf[0][1] = temp

        temp          = self.bf[0][2]
        self.bf[0][2] = self.lf[0][2]
        self.lf[0][2] = self.ff[0][2]
        self.ff[0][2] = self.rf[0][2]
        self.rf[0][2] = temp

    def D(self):
        temp          = self.df[0][0]
        self.df[0][0] = self.df[2][0]
        self.df[2][0] = self.df[2][2]
        self.df[2][2] = self.df[0][2]
        self.df[0][2] = temp

        temp          = self.df[0][1]
        self.df[0][1] = self.df[1][0]
        self.df[1][0] = self.df[2][1]
        self.df[2][1] = self.df[1][2]
        self.df[1][2] = temp

        temp          = self.ff[2][0]
        self.ff[2][0] = self.lf[2][0]
        self.lf[2][0] = self.bf[2][0]
        self.bf[2][0] = self.rf[2][0]
        self.rf[2][0] = temp

        temp          = self.ff[2][1]
        self.ff[2][1] = self.lf[2][1]
        self.lf[2][1] = self.bf[2][1]
        self.bf[2][1] = self.rf[2][1]
        self.rf[2][1] = temp

        temp          = self.ff[2][2]
        self.ff[2][2] = self.lf[2][2]
        self.lf[2][2] = self.bf[2][2]
        self.bf[2][2] = self.rf[2][2]
        self.rf[2][2] = temp

    def R(self):
        temp          = self.rf[0][0]
        self.rf[0][0] = self.rf[2][0]
        self.rf[2][0] = self.rf[2][2]
        self.rf[2][2] = self.rf[0][2]
        self.rf[0][2] = temp

        temp          = self.rf[0][1]
        self.rf[0][1] = self.rf[1][0]
        self.rf[1][0] = self.rf[2][1]
        self.rf[2][1] = self.rf[1][2]
        self.rf[1][2] = temp

        temp          = self.uf[0][2]
        self.uf[0][2] = self.ff[0][2]
        self.ff[0][2] = self.df[0][2]
        self.df[0][2] = self.bf[2][0]
        self.bf[2][0] = temp

        temp          = self.uf[1][2]
        self.uf[1][2] = self.ff[1][2]
        self.ff[1][2] = self.df[1][2]
        self.df[1][2] = self.bf[1][0]
        self.bf[1][0] = temp

        temp          = self.uf[2][2]
        self.uf[2][2] = self.ff[2][2]
        self.ff[2][2] = self.df[2][2]
        self.df[2][2] = self.bf[0][0]
        self.bf[0][0] = temp

    def L(self):
        temp          = self.lf[0][0]
        self.lf[0][0] = self.lf[2][0]
        self.lf[2][0] = self.lf[2][2]
        self.lf[2][2] = self.lf[0][2]
        self.lf[0][2] = temp

        temp          = self.lf[0][1]
        self.lf[0][1] = self.lf[1][0]
        self.lf[1][0] = self.lf[2][1]
        self.lf[2][1] = self.lf[1][2]
        self.lf[1][2] = temp

        temp          = self.uf[0][0]
        self.uf[0][0] = self.bf[2][2]
        self.bf[2][2] = self.df[0][0]
        self.df[0][0] = self.ff[0][0]
        self.ff[0][0] = temp

        temp          = self.uf[1][0]
        self.uf[1][0] = self.bf[1][2]
        self.bf[1][2] = self.df[1][0]
        self.df[1][0] = self.ff[1][0]
        self.ff[1][0] = temp

        temp          = self.uf[2][0]
        self.uf[2][0] = self.bf[0][2]
        self.bf[0][2] = self.df[2][0]
        self.df[2][0] = self.ff[2][0]
        self.ff[2][0] = temp

    def F(self):
        temp          = self.ff[0][0]
        self.ff[0][0] = self.ff[2][0]
        self.ff[2][0] = self.ff[2][2]
        self.ff[2][2] = self.ff[0][2]
        self.ff[0][2] = temp

        temp          = self.ff[0][1]
        self.ff[0][1] = self.ff[1][0]
        self.ff[1][0] = self.ff[2][1]
        self.ff[2][1] = self.ff[1][2]
        self.ff[1][2] = temp

        temp          = self.uf[2][0]
        self.uf[2][0] = self.lf[2][2]
        self.lf[2][2] = self.df[0][2]
        self.df[0][2] = self.rf[0][0]
        self.rf[0][0] = temp

        temp          = self.uf[2][1]
        self.uf[2][1] = self.lf[1][2]
        self.lf[1][2] = self.df[0][1]
        self.df[0][1] = self.rf[1][0]
        self.rf[1][0] = temp

        temp          = self.uf[2][2]
        self.uf[2][2] = self.lf[0][2]
        self.lf[0][2] = self.df[0][0]
        self.df[0][0] = self.rf[2][0]
        self.rf[2][0] = temp

    def B(self):
        temp          = self.bf[0][0]
        self.bf[0][0] = self.bf[2][0]
        self.bf[2][0] = self.bf[2][2]
        self.bf[2][2] = self.bf[0][2]
        self.bf[0][2] = temp

        temp          = self.bf[0][1]
        self.bf[0][1] = self.bf[1][0]
        self.bf[1][0] = self.bf[2][1]
        self.bf[2][1] = self.bf[1][2]
        self.bf[1][2] = temp

        temp          = self.uf[0][0]
        self.uf[0][0] = self.rf[0][2]
        self.rf[0][2] = self.df[2][2]
        self.df[2][2] = self.lf[2][0]
        self.lf[2][0] = temp

        temp          = self.uf[0][1]
        self.uf[0][1] = self.rf[1][2]
        self.rf[1][2] = self.df[2][1]
        self.df[2][1] = self.lf[1][0]
        self.lf[1][0] = temp

        temp          = self.uf[0][2]
        self.uf[0][2] = self.rf[2][2]
        self.rf[2][2] = self.df[2][0]
        self.df[2][0] = self.lf[0][0]
        self.lf[0][0] = temp

    def Up(self):
        for _ in range(3):
            self.U()

    def Dp(self):
        for _ in range(3):
            self.U()

    def Rp(self):
        for _ in range(3):
            self.U()

    def Lp(self):
        for _ in range(3):
            self.U()

    def Fp(self):
        for _ in range(3):
            self.U()

    def Bp(self):
        for _ in range(3):
            self.U()

    def draw(self, model):
        self.draw_face(model, 3, 0, self.uf)
        self.draw_face(model, 3, 6, self.df)
        self.draw_face(model, 0, 3, self.lf)
        self.draw_face(model, 3, 3, self.ff)
        self.draw_face(model, 6, 3, self.rf)
        self.draw_face(model, 9, 3, self.bf)

    def draw_face(self, model, x, y, face):
        for i in range(3):
            for j in range(3):
                model.set_pixel(y+j, x+i, face[j][i])
