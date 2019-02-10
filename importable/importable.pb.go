// Code generated by protoc-gen-go. DO NOT EDIT.
// source: importable.proto

// Test to make sure that importing other packages doesnt break

package importable

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion2 // please upgrade the proto package

type Msg struct {
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *Msg) Reset()         { *m = Msg{} }
func (m *Msg) String() string { return proto.CompactTextString(m) }
func (*Msg) ProtoMessage()    {}
func (*Msg) Descriptor() ([]byte, []int) {
	return fileDescriptor_821aa36cec5cc38d, []int{0}
}

func (m *Msg) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Msg.Unmarshal(m, b)
}
func (m *Msg) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Msg.Marshal(b, m, deterministic)
}
func (m *Msg) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Msg.Merge(m, src)
}
func (m *Msg) XXX_Size() int {
	return xxx_messageInfo_Msg.Size(m)
}
func (m *Msg) XXX_DiscardUnknown() {
	xxx_messageInfo_Msg.DiscardUnknown(m)
}

var xxx_messageInfo_Msg proto.InternalMessageInfo

func init() {
	proto.RegisterType((*Msg)(nil), "twirptest.importable.Msg")
}

func init() { proto.RegisterFile("importable.proto", fileDescriptor_821aa36cec5cc38d) }

var fileDescriptor_821aa36cec5cc38d = []byte{
	// 101 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xe2, 0x12, 0xc8, 0xcc, 0x2d, 0xc8,
	0x2f, 0x2a, 0x49, 0x4c, 0xca, 0x49, 0xd5, 0x2b, 0x28, 0xca, 0x2f, 0xc9, 0x17, 0x12, 0x29, 0x29,
	0xcf, 0x2c, 0x2a, 0x28, 0x49, 0x2d, 0x2e, 0xd1, 0x43, 0xc8, 0x29, 0xb1, 0x72, 0x31, 0xfb, 0x16,
	0xa7, 0x1b, 0x39, 0x73, 0x31, 0x07, 0x97, 0x25, 0x0b, 0xd9, 0x70, 0xb1, 0x04, 0xa7, 0xe6, 0xa5,
	0x08, 0x49, 0xea, 0x61, 0x53, 0xac, 0xe7, 0x5b, 0x9c, 0x2e, 0x85, 0x5b, 0xca, 0x89, 0x27, 0x8a,
	0x0b, 0x21, 0x92, 0xc4, 0x06, 0xb6, 0xd6, 0x18, 0x10, 0x00, 0x00, 0xff, 0xff, 0xf2, 0x28, 0xb2,
	0x9e, 0x8a, 0x00, 0x00, 0x00,
}
