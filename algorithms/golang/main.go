package main

import (
	"crypto/cipher"
	"crypto/des"
	"crypto/md5"
	"encoding/base64"
	"fmt"
	"strings"
)

func main() {
	str := "T80AEExYvXrCJ7iDx7ndzQ=="
	UnHash(&str)
	fmt.Println(str)
}

func UnHash(s *string) error {
	var err error
	salt := []byte{byte(0xc7), byte(0x73), byte(0x21),
		byte(0x8c), byte(0x7e), byte(0xc8),
		byte(0xee), byte(0x99)}
	password := "AESIsFipsPub197"
	iterations := 2048

	*s, err = Decrypt(password, iterations, *s, salt)
	if err != nil {
		return err
	}
	return nil
}

func Decrypt(password string, obtenationIterations int, cipherText string, salt []byte) (string, error) {
	msgBytes, err := base64.StdEncoding.DecodeString(cipherText)
	if err != nil {
		return "", err
	}

	dk, iv := getDerivedKey(password, salt, obtenationIterations)
	block, err := des.NewCipher(dk)
	if err != nil {
		return "", err
	}

	decrypter := cipher.NewCBCDecrypter(block, iv)
	decrypted := make([]byte, len(msgBytes))
	decrypter.CryptBlocks(decrypted, msgBytes)

	decryptedString := strings.TrimRight(string(decrypted), "\x01\x02\x03\x04\x05\x06\x07\x08")

	return decryptedString, nil
}

func getDerivedKey(password string, salt []byte, count int) ([]byte, []byte) {
	key := md5.Sum([]byte(password + string(salt)))
	for i := 0; i < count-1; i++ {
		key = md5.Sum(key[:])
	}
	return key[:8], key[8:]
}
