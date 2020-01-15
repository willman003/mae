from werkzeug.security import generate_password_hash, check_password_hash
from . import db



#------CLASS cho Web bán hàng------#
class Loai_san_pham(db.Model):
    __tablename__ = 'loai_san_pham'
    ma_loai = db.Column(db.Integer(), nullable = False, primary_key = True)
    ten_loai = db.Column(db.String(50), nullable = False)
    mo_ta = Column(db.Text())
    
    def __str__(self):
        return self.ten_category

class San_pham(db.Model):
    __tablename__ = 'san_pham'
    ma_san_pham = db.Column(db.Integer(), nullable = False, primary_key = True)
    ten_san_pham = Column(String(100), nullable = False)
    ma_loai = Column(Integer, ForeignKey('loai_san_pham.ma_loai'))
    gia_ban = Column(Integer, nullable = False)
    gia_nhap = Column(Integer, nullable = False, default = 0)
    so_luong_ton = Column(Integer, nullable = False, default = 0)
    id_sendo = Column(Integer)
    thuoc_tinh = Column(String(200))
    
    loai_san_pham = relationship(Loai_san_pham, backref='san_pham')
    def __str__(self):
        return self.ten_san_pham

class Loai_nguoi_dung(Base):
    __tablename__ = 'loai_nguoi_dung'
    ma_loai_nguoi_dung = Column(Integer, nullable = False, primary_key = True)
    ten_loai_nguoi_dung = Column(String(100), nullable = False)
    def __str__(self):
        return self.ten_loai_nguoi_dung


class Nguoi_dung(Base):
    __tablename__ = 'nguoi_dung'
    ma_nguoi_dung = Column(Integer, nullable = False, primary_key = True)
    ma_loai_nguoi_dung = Column(Integer, ForeignKey('loai_nguoi_dung.ma_loai_nguoi_dung'))
    ho_ten = Column(String(200))
    ten_dang_nhap = Column(String(64), nullable = False)
    mat_khau_hash = Column(String(128), nullable = False)
    
    loai_nguoi_dung = relationship(Loai_nguoi_dung,backref='nguoi_dung') 
    @property
    def is_authenticated(self):
        return True
    @property
    def is_active(self):
        return True
    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return self.ma_nguoi_dung

    def __unicode__(self):
        return self.ho_ten
    
    def __str__(self):
        return self.ten_dang_nhap
   

class Khach_hang(Base):
    __tablename__ = 'khach_hang'
    ma_khach_hang = Column(Integer, nullable = False, primary_key = True)
    ten_khach_hang = Column(String(100), nullable = False)
    email=Column(String(100))
    dia_chi = Column(String(200), nullable = False)
    dien_thoai = Column(String(20), nullable = False)
    
    def __str__(self):
        return self.ten_khach_hang

class Hoa_don(Base):
    __tablename__ = 'hoa_don'
    ma_hoa_don = Column(Integer, nullable = False, primary_key = True)
    ngay_tao_hoa_don = Column(DateTime, nullable = False)
    ma_khach_hang = Column(Integer, ForeignKey('khach_hang.ma_khach_hang'))
    tong_tien = Column(Float, nullable = False)
    trang_thai = Column(Integer)
    khach_hang = relationship(Khach_hang, backref = 'hoa_don')
    def __repr__(self):
        return "<Ma_hoa_don = %d>" % self.ma_hoa_don

class Don_hang(Base):
    __tablename__ = 'don_hang'
    id = Column(Integer, nullable =False, primary_key = True)
    ma_hoa_don = Column(Integer, ForeignKey('hoa_don.ma_hoa_don'))
    ma_san_pham = Column(Integer, ForeignKey('san_pham.ma_san_pham'))
    ten_san_pham = Column(String(100), nullable = False)
    so_luong = Column(Integer, nullable = False)
    don_gia = Column(Integer, ForeignKey('san_pham.gia_ban'))
    hoa_don = relationship(Hoa_don, backref = 'don_hang', foreign_keys=[ma_hoa_don])
    san_pham = relationship(San_pham, backref = 'don_hang', foreign_keys=[ma_san_pham])
    
    def __repr__(self):
        return "<Ma_hoa_don = %d>" % self.ma_hoa_don


engine = create_engine('sqlite:///Mae/du_lieu/ql_mae.db?check_same_thread=False')
Base.metadata.create_all(engine)



